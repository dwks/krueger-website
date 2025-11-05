#!/bin/sh
source env/bin/activate
git pull && make && rm -rf /var/www/html && cp -ar dist /var/www/html
