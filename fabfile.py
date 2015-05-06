import fabric
from fabric.contrib import project
from fabric.api import local, cd
from fabric.state import env
from src.mysite.settings import STATIC_ROOT, BASE_DIR

# to use ~/.ssh/config
# but in circleci.com -> project settings -> SSH Permisions
# Just put the aws key there then, it works.
env.use_ssh_config = True
env.hosts = ['ec2-52-74-40-130.ap-southeast-1.compute.amazonaws.com']

# Where the static files get collected locally. Your STATIC_ROOT setting.
env.local_static_root = STATIC_ROOT
env.remote_static_root = '/git-repos/myweb/mysite/static'


def deploy(where='local', branch='staging'):
    """
    build containers on local using fabric local(), lcd(),
    or remote using fabric run(), cd()
    RUN: fab deploy:where=local, branch=staging
    RUN: fab deploy:where=local, branch=production
    """
    if where == 'local':
        deploy_run = getattr(fabric.api, 'local')
        deploy_cd = getattr(fabric.api, 'lcd')
    elif where == 'remote':
        deploy_run = getattr(fabric.api, 'run')
        deploy_cd = getattr(fabric.api, 'cd')
    # env
    branch_fullpath = '/git-repos/myweb.branch.{0}'.format(branch)
    git_url = "https://github.com/liaozd/myweb.git"
    # clean before deploy
    deploy_run('rm -rf {0}'.format(branch_fullpath))
    deploy_run('mkdir -p /git-repos')
    deploy_run('git clone -b {branch} --single-branch {url} {path}'.format(branch=branch, url=git_url, path=branch_fullpath))

    deploy_commands = [
        'uname -nvr', # show maching info
        # rebuild docker containers
        'docker-compose --file docker-compose.{0}.yml build'.format(branch),
        # clean image name/tag with '<none>'
        'docker-compose stop',
        'export IMAGENONE=$(docker images -q --filter "dangling=True"); [ -z "$IMAGENONE"  ] || docker rmi -f $IMAGENONE',
        'docker-compose --verbose --project-name myweb --file docker-compose.{0}.yml up -d'.format(branch),
        'sleep 4', # wait the db container boot up
        # migrate the django database
        'docker exec myweb_{0}_1 python /git-repos/myweb/src/manage.py migrate'.format(branch),
        #TODO createsuperuser none interactive
        'echo "docker exec -ti myweb_{0}_1 bash"'.format(branch),
        'echo "python /git-repos/myweb/src/manage.py createsuperuser --username liao --email liao_zd@hotmail.com"',
    ]

    with deploy_cd(branch_fullpath):
        for command in deploy_commands:
            deploy_run(command)


def deploy_static():
    local(BASE_DIR + '/manage.py collectstatic --noinput -v3 --clear')
    project.rsync_project(
        remote_dir=env.remote_static_root,
        local_dir=env.local_static_root,
        # delete=True # <-- Be careful with this
    )

