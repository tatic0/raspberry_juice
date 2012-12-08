#!/usr/bin/env python
# cpu_load.py

import time, sys

def cpusage():
  clock = 0
  counter = 1
  #data = 0.00
  while True:
    cpu = open('/proc/loadavg','r')
    datafilename = "cpu-%d.data" %counter
    #print(datafilename)
    graph = open(datafilename,'a')
    data = cpu.read()
    #print(clock, data[0:4])
    line = str(clock) + " " + str(data[0:4]) + "\n" 
    graph.write(line)
    graph.close()
    cpu.close()
    time.sleep(5)
    clock +=1
    if clock == 600:
      clock =0
      counter +=1

def main():
  cpusage()

#if __name__ == "__main__":
#  try:
#    #cpusage()
#    main()
#  except KeyboardInterrupt:
#    print("Quitting application")
#    sys.exit(0)