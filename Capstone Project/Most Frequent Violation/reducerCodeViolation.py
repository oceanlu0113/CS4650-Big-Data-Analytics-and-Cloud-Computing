#!/usr/bin/python

import sys
#set variables for code violation description and count
currCode = None
currCount = 0

for line in sys.stdin:
	code, count = line.split('\t')
    # after splitting code and count, we need to make sure count is an int
	count = int(count)
    #if there are instances of code, then we increment the count
    # if not, then we go to the next lineand update the values
	if code == currCode:
        currCount += count
  	else:
    		if currCode:
      			print('{0}\t{1}'.format(currCode, currCount))
    		currCode = code
    		currCount = count
if currCode == code:
	print('{0}\t{1}'.format(currCode, currCount))
