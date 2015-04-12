# myweb
personal website + blog

# 
#TODO put in init
cd ~/git-repos/myweb/mysite/

gunicorn --chdir src mysite.wsgi:application --bind=127.0.0.1:8020 --workers 1 --daemon --reload

# fabric deploy static file
# clear the settings.STATIC_ROOT folder and collectstatic into it
fab deploy_static
