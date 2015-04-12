from fabric.api import *
from fabric.contrib import project
from mysite.settings import STATIC_ROOT, BASE_DIR

env.roledefs['static'] = ['ubuntu@52.74.40.130', ]
# Where the static files get collected locally. Your STATIC_ROOT setting.
env.local_static_root = STATIC_ROOT

env.remote_static_root = '/home/ubuntu/git-repos/myweb/mysite/static'
@roles('static')
def deploy_static():
    local(BASE_DIR + '/manage.py collectstatic --noinput -v3 --clear')
    project.rsync_project(
        remote_dir=env.remote_static_root,
        local_dir=env.local_static_root,
        # delete=True # <-- Be careful with this
    )

