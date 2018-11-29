#!/bin/bash

service=postgresql
if (( $(ps -ef | grep -v grep | grep $service | wc -l) > 0 ))
then
    echo "$service is running!!!"
else
    echo "Starting $service."
    /etc/init.d/$service start
fi

./manage.py runserver 0.0.0.0:8000
