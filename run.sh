#!/bin/bash
rm -rf celerybeat*
rm -rf log/celery_job_info*
docker-compose up
