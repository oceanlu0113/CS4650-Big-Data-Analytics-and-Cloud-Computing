#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    if len(line) >=2:
        date = line[1]
        print ("%s\t%s"% (date, 1))

'''
#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    if len(line) >=2:
        plate = line[5]
        print ("%s\t%s"% (plate, 1))
"""

"""
#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    if len(line) >=2:
        location = line[11]
        print ("%s\t%s"% (location, 1))

'''