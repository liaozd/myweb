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
    'docker-compose up -d',
    # clean image name/tag with '<none>'
    'export IMAGENONE=$(docker images -q --filter "dangling=True"); [ -z "$IMAGENONE"  ] || docker rmi -f $IMAGENONE',
    # migrate the django database
    'docker exec myweb_web_1 python /git-repos/myweb/src/manage.py migrate',
]


def local_deploy():
    """build containers on local dev"""
    for command in build_commands:
        local(command)
    # local("""docker exec myweb_web_1 echo 'from django.contrib.auth.models import User; User.objects.create_superuser("liao", "liao_zd@hotmail.com", "pass")' | /git-repos/myweb/src/manage.py shell""")
    local("""CMD='echo "from django.contrib.auth.models import User; User.objects.create_superuser({0}, {1}, {2})" | /git-repos/myweb/src/manage.py shell'; docker exec myweb_web_1 $CMD""".format("liao", "liao_zd@hotmail.com", "pass"))




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