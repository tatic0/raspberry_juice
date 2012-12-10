#!/bin/bash
# launcher.sh

python cpu_load.py &
while true; do if [[ ! $(ps -ef |egrep "python.*[m]ain") ]] ; then echo "server down"; ./main.py; fi; sleep 10; done
