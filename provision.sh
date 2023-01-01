#!/usr/bin/env bash
yum update
yum -y install nginx
yum install -y python3 python3-request* python3-http*
pip3 install --user --upgrade pip
pip3 install --user setuptools_rust pyopenssl http1 requests pandas
sudo mkdir -p /etc/nginx/sites-enabled
sudo cp /vagrant/default /etc/nginx/sites-enabled/default
service nginx start
