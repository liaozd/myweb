[![Circle CI](https://circleci.com/gh/liaozd/myweb/tree/production.svg?style=svg)](https://circleci.com/gh/liaozd/myweb/tree/production)

# myweb
blog + app

two nginx containers running at the same time, production and staging, source codes are ADD to the containers.
postgres container running for both
data container for loging or maybe postgres database files


gunicorn --chdir src mysite.wsgi:application --bind=127.0.0.1:8020 --workers 1 --daemon --reload

# fabric deploy static file
# clear the settings.STATIC_ROOT folder and collectstatic into it
fab deploy_static
