#!/bin/bash

cd /usr/src/app/mimic

git fetch --all
git checkout mimic-csv2
git pull

exec "$@"
