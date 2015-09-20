import os
from os.path import dirname, basename
import fabric
from fabric.contrib import project
from fabric.api import local, cd
from fabric.state import env
from src.conf.settings.base import STATIC_ROOT, BASE_DIR

# In local dev, to load "~/.ssh/config" file
# While in circleci.com
# put the aws key in: project settings -> SSH Permissions,
env.use_ssh_config = True
# set $MYSERVER in CI or in the environment file
env.hosts = os.environ['MYSERVER']

# Where the static files get collected locally. Your STATIC_ROOT setting.
env.local_static_root = STATIC_ROOT
env.remote_static_root = os.path.join(BASE_DIR, 'static/')


def deploy(to='local', branch='staging'):
    """
    build containers on local using fabric local(), lcd(),
    or remote using fabric run(), cd()
    RUN: fab deploy:to=local,branch=production
    RUN: fab deploy:to=remote,branch=staging
    RUN: fab deploy:to=remote,branch=production
    """
    print " Deploying {0} branch to {1} ".format(branch, to).center(70, '#')
    if to == 'local':
        deploy_run = getattr(fabric.api, 'local')
        deploy_cd = getattr(fabric.api, 'lcd')
    elif to == 'remote':
        deploy_run = getattr(fabric.api, 'run')
        deploy_cd = getattr(fabric.api, 'cd')

    # Consider of build environment in CI, hard code on the git_repos_path
    git_repos_path = "/git-repos/myweb"
    git_repos_root_path = dirname(git_repos_path)
    git_project_name = basename(git_repos_path)
    branch_path = '{fullpath_prefix}.branch.{branch}'.format(fullpath_prefix=git_repos_path, branch=branch)
    # branch_path should be like: /git-repos/myweb.branch.dev/
    git_url = 'https://github.com/liaozd/{0}.git'.format(git_project_name)
    docker_exec_prefix = 'docker-compose --verbose --project-name {project_name} --file docker-compose.{branch}.yml'.\
        format(project_name=git_project_name, branch=branch)

    # clean everything before deploy
    deploy_run('rm -rf {0}'.format(branch_path))
    deploy_run('mkdir -p {0}'.format(git_repos_root_path))
    deploy_run(
        'git clone --quiet --branch {branch} --single-branch {url} {path}'.format(branch=branch,
                                                                                  url=git_url,
                                                                                  path=branch_path))

    deploy_commands = [
        'uname -nvr',  # show machine info

        # generate different docker-compose file for different branches
        'sh docker-compose-generator.sh',

        # generate Dockerfile for different projects and environments
        'sh dockerfile-generator.sh',

        # rebuild docker containers
        '{0} build'.format(docker_exec_prefix),
        # clean image name/tag with '<none>'
        '{0} stop'.format(docker_exec_prefix),
        'IMAGES_NONE=$(docker images -q --filter "dangling=True"); \
         [ -z "$IMAGES_NONE"  ] || docker rmi -f $IMAGES_NONE',

        # TODO consider backup/restore your data in the db container
        # TODO wait for DB_CONTAINER ready
        # TODO sleep is not need in CI/aws, but need a few secs in local dev, I don't know why
        '[ -n "$DB_CONTAINER"  ] || \
        export DB_CONTAINER=$(docker run -e "POSTGRES_PASSWORD=pass" -d --restart=always --name db postgres); \
        sleep 7',
        # wait for db container ready

        '{0} up -d'.format(docker_exec_prefix),

        # migrate the django database
        'docker exec {project_name}_{branch}_1 python /git-repos/{project_name}/src/manage.py migrate'.\
            format(project_name=git_project_name, branch=branch),
        # TODO createsuperuser none interactive
        'echo "docker exec -ti {project_name}_{branch}_1 bash"'.format(project_name=git_project_name, branch=branch),
        'echo "python /git-repos/{project_name}/src/manage.py createsuperuser --username liao --email liao_zd@hotmail.com"'.\
            format(project_name=git_project_name),
        # deploy static files
        'docker exec {project_name}_{branch}_1 python /git-repos/{project_name}/src/manage.py collectstatic --noinput -v3'.\
            format(project_name=git_project_name, branch=branch),
    ]

    with deploy_cd(branch_path):
        for command in deploy_commands:
            deploy_run(command)


def deploy_static():
    local(BASE_DIR + '/manage.py collectstatic --noinput -v3 --clear')
    project.rsync_project(
        remote_dir=env.remote_static_root,
        local_dir=env.local_static_root,
        # delete=True # <-- Be careful with this
    )
