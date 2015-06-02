############################################################
# Dockerfile to build Nginx Installed Containers
# ref: https://github.com/nginxinc/docker-nginx/blob/e9202a4795d84a85499fcd6cda58ddde4cf4079d/Dockerfile
############################################################

FROM debian:wheezy
MAINTAINER Liao Zhuodi <liao_zd@hotmail.com>

RUN echo 'Asia/Shanghai' > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata

# Add application repository URL to the default sources
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62
RUN echo "deb http://nginx.org/packages/mainline/debian/ wheezy nginx" >> /etc/apt/sources.list
# Update the repository
RUN apt-get -yq update
RUN apt-get -yq install \
    python python-pip python-dev \
    supervisor

# psycopg2 Python-PostgreSQL Database Adapter dependency packages
RUN apt-get -yq install libpq-dev

# INSTALL NGINX
RUN apt-get install -yq nginx
RUN rm -f /etc/nginx/conf.d/*
# Append "daemon off;" to the beginning of the configuration
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

ENV PYTHONUNBUFFERED 1

ENV CODEPATH /git-repos/myweb
WORKDIR $CODEPATH
ADD . .
RUN pip install -r conf.d/requirements/docker-web-container.txt
RUN ln -sf $CODEPATH/conf.d/nginx/myweb_nginx.conf /etc/nginx/conf.d/
RUN ln -sf $CODEPATH/conf.d/supervisor/supervisor.conf /etc/supervisor/conf.d/

##################################################
# tools for debuging, this is just for temporary
# RUN apt-get -qq install vim
# RUN apt-get -qq install tree
# RUN apt-get -qq install procps
# RUN apt-get install -qq postgresql-client
##################################################

cmd ["/usr/bin/supervisord", "-n"]