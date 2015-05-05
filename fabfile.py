from fabric.api import *
from fabric.contrib import project
from fabric.operations import local
from src.mysite.settings import STATIC_ROOT, BASE_DIR

env.hosts = ['ec2-52-74-40-130.ap-southeast-1.compute.amazonaws.com']
# to use ~/.ssh/config
# but in circleci.com -> project settings -> SSH Permisions
# Just put the aws key there then, it works.
env.use_ssh_config = True

# Where the static files get collected locally. Your STATIC_ROOT setting.
env.local_static_root = STATIC_ROOT
env.remote_static_root = '/git-repos/myweb/mysite/static'


def deploy_static():
    local(BASE_DIR + '/manage.py collectstatic --noinput -v3 --clear')
    project.rsync_project(
        remote_dir=env.remote_static_root,
        local_dir=env.local_static_root,
        # delete=True # <-- Be careful with this
    )


build_commands = [
    'find -name *.pyc | xargs rm -f',
    # rebuild docker containers
    'docker-compose build',
    # clean image name/tag with '<none>'
    'docker-compose stop',
    'export IMAGENONE=$(docker images -q --filter "dangling=True"); [ -z "$IMAGENONE"  ] || docker rmi -f $IMAGENONE',
    'docker-compose up -d',
    'sleep 4', # wait the db container boot up
    # migrate the django database
    'docker exec myweb_web_1 python /git-repos/myweb/src/manage.py migrate',
    #TODO createsuperuser none interactive
    'echo "docker exec -ti myweb_web_1 bash"',
    'echo "python /git-repos/myweb/src/manage.py createsuperuser --username liao --email liao_zd@hotmail.com"',

]


def local_deploy():
    """build containers on local dev"""
    local('docker rm -f $(docker ps -aq)')
    for command in build_commands:
        local(command)
    # local("""docker exec myweb_web_1 echo 'from django.contrib.auth.models import User; User.objects.create_superuser("liao", "liao_zd@hotmail.com", "pass")' | /git-repos/myweb/src/manage.py shell""")


def init_build():
    run('rm -rf /git-repos/myweb')
    run('mkdir -p /git-repos')
    with cd('/git-repos'):
        run('git clone https://github.com/liaozd/myweb.git')


def deploy():
    with cd('/git-repos/myweb'):
        run('git pull')
        for command in build_commands:
            run(command)