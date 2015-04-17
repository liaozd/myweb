############################################################
# Dockerfile to build Nginx Installed Containers
# https://github.com/nginxinc/docker-nginx/blob/e9202a4795d84a85499fcd6cda58ddde4cf4079d/Dockerfile
############################################################

# Set the base image to Ubuntu
FROM debian:wheezy

MAINTAINER Liao Zhuodi <liao_zd@hotmail.com>

RUN echo 'Asia/Shanghai' > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata

# Install Nginx
# Add application repository URL to the default sources
RUN apt-key adv --keyserver pgp.mit.edu --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62
RUN echo "deb http://nginx.org/packages/mainline/debian/ wheezy nginx" >> /etc/apt/sources.list
# Update the repository
RUN apt-get -qq update
RUN apt-get -qq install \
    python python-pip python-dev \
    supervisor

# Install necessary tools, this is tempor
RUN apt-get -qq install tree procps

# psycopg2 Python-PostgreSQL Database Adapter dependency packages
RUN apt-get -qq install libpq-dev

# Download and Install Nginx
RUN apt-get install -qq nginx
RUN rm -f /etc/nginx/conf.d/*

# Append "daemon off;" to the beginning of the configuration
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Expose ports
EXPOSE 80 443

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /git-repos/myweb
WORKDIR /git-repos/myweb
ADD . .
RUN pip install -r /git-repos/myweb/src/requirements/base.txt
RUN ln -sf /git-repos/myweb/deployment/myweb_nginx.conf /etc/nginx/conf.d/
RUN ln -sf /git-repos/myweb/supervisor.conf /etc/supervisor/conf.d/

# Set the default command to execute
# when creating a new container
cmd ["supervisord", "-n"]

