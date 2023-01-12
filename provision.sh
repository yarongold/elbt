#!/usr/bin/env bash
yum update
yum -y install nginx
yum install -y python3 python3-request* python3-http*
pip3 install --user --upgrade pip
pip3 install --user setuptools_rust pyopenssl http1 requests pandas
sudo mkdir -p /etc/nginx/sites-enabled
sudo mkdir -p /etc/nginx/ssl
sudo cp /vagrant/ssl/* /etc/nginx/ssl
sudo setsebool -P httpd_can_network_connect 1
sudo mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.old
sudo cp /srv/src/nginx.conf /etc/nginx/nginx.conf
service nginx start
systemctl enable nginx
