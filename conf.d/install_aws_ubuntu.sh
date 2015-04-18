#!/usr/bin/env bash
# sudo run this

apt-get update
apt-get -y upgrade

# support utf-8
apt-get install -y language-pack-UTF-8
locale-gen UTF-8
dpkg-reconfigure locales

# set timezone
echo 'Asia/Shanghai' | tee /etc/timezone
dpkg-reconfigure --frontend noninteractive tzdata

# install nginx
apt-get -y install nginx

# install python-pip
apt-get install -y python-pip python-dev

# install package needed
apt-get install -y tree nmap vim htop

# vim settings
git clone git://github.com/amix/vimrc.git ~/.vim_runtime
sh ~/.vim_runtime/install_basic_vimrc.sh

# setup drone.io ci
git clone https://github.com/liaozd/myweb.git /tmp/myweb_droneio_deployment/