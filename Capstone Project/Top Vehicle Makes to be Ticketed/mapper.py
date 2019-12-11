#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    if len(line) >=2:
        make = line[8]
        print ("%s\t%s"% (make, 1))

