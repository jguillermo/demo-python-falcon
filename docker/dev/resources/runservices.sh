#!/bin/bash

xray-daemon -o -b localhost:2000 -n $DEPLOY_REGION &
/usr/sbin/nginx -g 'daemon off;' &
gunicorn -c /resources/gunicorn.py wsgi:api
