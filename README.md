# myweb
personal website

cd ~/git-repos/myweb/mysite/
# minimum workers
gunicorn mysite.wsgi:application --bind=127.0.0.1:8020 --workers 1 --daemon
