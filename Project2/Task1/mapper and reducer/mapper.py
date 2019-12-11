#!/usr/bin/env python
# coding: utf-8

import re
import sys

# "line" will iterate over each line of text read from standard input
for line in sys.stdin:
# removing all leading and trailing whitespace
  if line.strip():
  # Substituting everything besides letters with a space
    line = re.sub('[^a-zA-Z\n]', ' ', line)
	# Splitting the "line" into its separate words and storing each as an element in a list
    line = line.split()
	# For each word in the list print out a key value pair delimited by a tab i.e intermediate values
    for word in line:
      print("%s\t%s"% (word, 1))