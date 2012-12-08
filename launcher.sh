#!/bin/bash
# launcher.sh

while true; do if [[ ! $(ps -ef |egrep "python.*[m]ain") ]] ; then echo "server down"; ./main.py; fi; sleep 10; done
