#!/usr/bin/env python
# coding: utf-8

"""
import sys

totalCount = 0
prevWord = None
newList = {}

# "line" will iterate over each line of text read from standard input (Will receive intermediate key-value pairs from mapper after the sort and shuffle phase)
for line in sys.stdin:
# Saving key-value pair into array where the first element is the word and the second is 1
  line = line.split()
  #if we have encountered our first word yet and if the previoius word was different from the one currently being read in output the word and the total number of occurences of that word
  if prevWord and prevWord != line[0]:
    if prevWord in newList:
	  #print("%s\t%s"% (prevWord, totalCount))
	  #totalCount = 0
	  newList[prevWord] = newList[prevWord] + totalCount
    else:
      newList[prevWord] = totalCount
    totalCount = 0
    
  prevWord = line[0]
  totalCount = totalCount float(line[1])
# Ensures that we output the last line from standard input
if prevWord != None:
  if prevWord in newList:
	#print("%s\t%s"% (prevWord, totalCount))
    newList[prevWord] = newList[prevWord] + totalCount
    
reverseList = sorted(newList.items(), key = lambda x: x[1], reverse = True) 

#  Print the final list that we reversed
for key in reverseList: #gets each word in the the reverse list
  print(key) #prints each word

"""
import sys

#start without anything
curr_word = None
curr_count = 0

#go line by line
for line in sys.stdin:
	#every word/count is a tab over
	word, count = line.split('\t')
	#add to the number counted
	count = int(count)
	if word == curr_word:
		curr_count += count
	else:
		if curr_word:
			print('{0}\t{1}'.format(curr_word, curr_count))
		curr_word = word
		curr_count = count

if curr_word == word:
	print('{0}\t{1}'.format(curr_word, curr_count))

