#!/usr/bin/env bash

for i in $(seq 1 9); do   cp -v history.log.1.gz history.log.${i}.gz; done

files_to_rename=$(ls history.log.*gz)
echo $files_to_rename
history.log.1.gz history.log.2.gz history.log.3.gz history.log.4.gz history.log.5.gz history.log.6.gz history.log.7.gz history.log.8.gz history.log.9.gz
root@vboxuser-virtualbox:/home/vboxuser# for f in $files_to_rename; do mv ${f} ${f}.$(date +"%Y-%m-%d"); done