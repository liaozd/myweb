############################################################
# Dockerfile to build Nginx Installed Containers
# https://github.com/nginxinc/docker-nginx/blob/e9202a4795d84a85499fcd6cda58ddde4cf4079d/Dockerfile
############################################################
# BUILD-USING: docker build -t my_nginx_img .
# RUN-USING: docker run -d -p 80:80 --name my_nginx_cont my_nginx_img

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

# Install necessary tools
RUN apt-get -qq install vim tree procps

# psycopg2 Python-PostgreSQL Database Adapter dependency packages
RUN apt-get -qq install libpq-dev

# Download and Install Nginx
RUN apt-get install -qq nginx
# Remove the default Nginx configuration file
# RUN rm -v /etc/nginx/nginx.conf
# Copy a configuration file from the current directory
# ADD nginx.conf /etc/nginx/

# Append "daemon off;" to the beginning of the configuration
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Expose ports
EXPOSE 80

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD . /code

RUN pip install -r src/requirements/base.txt
RUN rm -f /etc/nginx/conf.d/*
RUN ln -sf /code/deployment/myweb_nginx.conf /etc/nginx/conf.d/
RUN ln -sf /code/supervisor.conf /etc/supervisor/conf.d/

# Set the default command to execute
# when creating a new container
cmd ["supervisord", "-n"]


