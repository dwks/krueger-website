#!/bin/bash
source env/bin/activate
git pull && make && sudo rm -rf /var/www/html && sudo cp -ar dist /var/www/html
