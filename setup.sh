#!/bin/bash
docker build -t iamforeverme/python2:1 crawls
docker-compose build
docker-compose run web python manage.py migrate