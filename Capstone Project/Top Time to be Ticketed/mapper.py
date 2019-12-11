#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    if len(line) >=2:
        time = line[2]
        print ("%s\t%s"% (time, 1))

