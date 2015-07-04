#!/bin/bash
set -e

docker build --rm -t {{ project_name }} .
COMPOSE="docker-compose -f docker-compose-prod.yml"
$COMPOSE up -d source
$COMPOSE logs source
