import fabric
from fabric.contrib import project
from fabric.api import local, cd
from fabric.state import env
from src.mysite.settings import STATIC_ROOT, BASE_DIR

# to use ~/.ssh/config
# but in circleci.com -> project settings -> SSH Permisions
# Just put the aws key there then, it works.
env.use_ssh_config = True
env.hosts = ['ec2-52-74-132-196.ap-southeast-1.compute.amazonaws.com']

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
    git_url = 'https://github.com/liaozd/myweb.git'
    docker_exec_prefix = 'docker-compose --verbose --project-name myweb --file docker-compose.{0}.yml'.format(branch)

    # clean everything before deploy
    deploy_run('rm -rf {0}'.format(branch_fullpath))
    deploy_run('mkdir -p /git-repos')
    deploy_run(
        'git clone -b {branch} --single-branch {url} {path}'.format(branch=branch, url=git_url, path=branch_fullpath))

    deploy_commands = [
        'uname -nvr',  # show machine info
        # rebuild docker containers
        '{0} build'.format(docker_exec_prefix),
        # clean image name/tag with '<none>'
        '{0} stop'.format(docker_exec_prefix),
        'export IMAGES_NONE=$(docker images -q --filter "dangling=True");\
        [ -z "$IMAGES_NONE"  ] || docker rmi -f $IMAGES_NONE',
        '{0} up -d'.format(docker_exec_prefix),
        'sleep 4',  # wait the db container boot up
        # migrate the django database
        'docker exec myweb_{0}_1 python /git-repos/myweb/src/manage.py migrate'.format(branch),
        # TODO createsuperuser none interactive
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