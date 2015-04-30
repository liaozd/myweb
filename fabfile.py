from fabric.api import *
from fabric.contrib import project
# from mysite.settings import STATIC_ROOT, BASE_DIR

# use ~/.ssh/config
# but in circleci.com -> project settings -> SSH Permisions
# Just put the aws key there then, it works.
env.use_ssh_config = True
env.roledefs = {
    'myweb': ['ec2-52-74-40-130.ap-southeast-1.compute.amazonaws.com']
}

# # Where the static files get collected locally. Your STATIC_ROOT setting.
# env.local_static_root = STATIC_ROOT
#
# env.remote_static_root = '/home/ubuntu/git-repos/myweb/mysite/static'
# @roles('aws_myweb')
# def deploy_static():
#     local(BASE_DIR + '/manage.py collectstatic --noinput -v3 --clear')
#     project.rsync_project(
#         remote_dir=env.remote_static_root,
#         local_dir=env.local_static_root,
#         # delete=True # <-- Be careful with this
#     )

@roles('myweb')
def up():
    # all commands need to be run under /git-repos/myweb
    commands = [
        'tail -n 150 /var/log/nginx/access.log',
        'git pull',
        # rebuild docker images
        'docker-compose build && docker-compose up -d',
        # clean image name with 'none'
        #TODO there are image name without none, exit with 1
        'docker rmi $(docker images | grep "^<none>" | awk '"'"'{print $3}'"'"')',
    ]

    for command in commands:
        with cd('/git-repos/myweb'):
            run(command)

