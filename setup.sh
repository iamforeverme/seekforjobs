#!/bin/bash
docker build -t iamforeverme/python2:1 crawls
docker-compose build
postgresDB=$(docker-compose run -d postgresDb)
sleep 15s
docker-compose run web python manage.py migrate
docker rm -f $postgresDB