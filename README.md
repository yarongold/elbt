# Home Assigment

#### Vagrant file based on CentOS 7
- Vagrant VM based on vshn/centos7
- Open port 80 for http
- Open port 443 for https
- Sync src folder
- Run provision script
- Run Python web service 

#### Provision shell script
- Install nginx
- install python packages
- Create required folders
- Copy self signed certificates for nginx ssl
- Open ports for nginx usage
- Copy nginx config file to setup reverse proxy with ssl
- Start nginx setvice
- Set nginx service automatic restart at machine boot


#### Self Signed certificates 
- Create self signed certificates for nginx ssl usage

#### Python app.py
- Call Jewish Calendar api using BaseHTTPRequestHandler
- Parse data
- Calculate qurter range using python pandas lib
- do_Get return json data

## References used:

### Jewish Calendar API: 
https://www.hebcal.com/home/195/jewish-calendar-rest-api

### Python Server Side Operations:
https://docs.python.org/3.9/library/ssl.html#server-side-operation
https://docs.python.org/3.9/library/socketserver.html#socketserver.request

### Python Pandas Quarter:
https://pandas.pydata.org/docs/reference/api/pandas.Period.quarter.html

### Vagrant centos box:
https://app.vagrantup.com/vshn/boxes/centos7

### NGINX SSL Termination:
https://docs.nginx.com/nginx/admin-guide/security-controls/terminating-ssl-http/

#### TO DO:
- Cleanup python warning 
