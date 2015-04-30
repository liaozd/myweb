from fabric.api import *
from fabric.contrib import project
# from mysite.settings import STATIC_ROOT, BASE_DIR

# use ~/.ssh/config
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
def log():
    run('tail -n 150 /var/log/docker/beijing_station.log')
