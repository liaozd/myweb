############################################################
# Dockerfile to build Nginx Installed Containers
# ref: https://github.com/nginxinc/docker-nginx/blob/e9202a4795d84a85499fcd6cda58ddde4cf4079d/Dockerfile
############################################################

FROM debian:wheezy
MAINTAINER Liao Zhuodi <liao_zd@hotmail.com>

RUN echo 'Asia/Shanghai' > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata

# Install nginx service
# Add application repository URL to the default sources
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62
RUN echo "deb http://nginx.org/packages/mainline/debian/ wheezy nginx" >> /etc/apt/sources.list
# Update the repository
RUN apt-get -y update
RUN apt-get -qq install \
    python python-pip python-dev \
    supervisor

# psycopg2 Python-PostgreSQL Database Adapter dependency packages
RUN apt-get -qq install libpq-dev

# Install nginx
RUN apt-get install -qq nginx
RUN rm -f /etc/nginx/conf.d/*
# Append "daemon off;" to the beginning of the configuration
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

ENV PYTHONUNBUFFERED 1

ADD conf.d/requirements/docker-web-container.txt .
RUN pip install -r docker-web-container.txt
ADD conf.d/nginx/myweb_nginx.conf /etc/nginx/conf.d/
ADD conf.d/supervisor/supervisor.conf /etc/supervisor/conf.d/

ENV SRC /git-repos/myweb
#RUN mkdir -p ${SRC}
WORKDIR $SRC


##################################################
# tools for debuging, this is just for temporary
RUN apt-get -qq install vim
# RUN apt-get -qq install tree
RUN apt-get -qq install procps
RUN apt-get install -qq postgresql-client
##################################################

cmd ["/usr/bin/supervisord", "-n"]