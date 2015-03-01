[![Build Status](https://drone.io/github.com/liaozd/myweb/status.png)](https://drone.io/github.com/liaozd/myweb/latest)

# myweb
personal website

# start gunicorn
#TODO put in init
cd ~/git-repos/myweb/mysite/
gunicorn mysite.wsgi:application --bind=127.0.0.1:8020 --workers 1 --daemon --reload

