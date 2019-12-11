#!/usr/bin/env python
# coding: utf-8

import sys

dictionary = {}
totalCount = 0
prevWord = None

# "line" will iterate over each line of text read from standard input (Will receive intermediate key-value pairs from mapper after the sort and shuffle phase)
for line in sys.stdin:
# Saving key-value pair into array where the first element is the word and the second is 1
  line = line.split()
  #if we have encountered our first word yet and if the previous word was different from the one currently being read in output the word and the total number of occurences of that word
  if prevWord and prevWord != line[0]:
    dictionary[prevWord] = totalCount
    totalCount = 0
    
  prevWord = line[0]
  totalCount += float(line[1])
# Ensures that we output the last line from standard input when word is same as previous
if prevWord != None:
  dictionary[prevWord] = totalCount
  
for words in sorted(dictionary, key=dictionary.get, reverse=True):
    print("%s\t%s"% (words,dictionary[words]))
