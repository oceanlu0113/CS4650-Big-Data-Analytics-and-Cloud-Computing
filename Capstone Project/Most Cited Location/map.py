#!/usr/bin/env python
# coding: utf-8
#This is python code that can be run anywhere in this code it stores certain parts of the columns into an array and then sorts it and prints it out
# essentially this code is like a hashmap that stores the total count and sorts it
import re
import sys
import pandas as pd


df = pd.read_csv(r"C:\Users\Jerry Trieu\Desktop\School\4650\Code\parking-citations.csv")
df = df["Issue Date"].dropna()

map = {}
arrayDate = []
arrayYear = []
arrayMonth = []
arrayState = []
arrayLocation = []

#Path to the CSV file
statedf = pd.read_csv(r"C:\Users\Jerry Trieu\Desktop\School\4650\Code\parking-citations.csv")
statedf = statedf["RP State Plate"].dropna()

#Path to the CSV file
locationdf = pd.read_csv(r"C:\Users\Jerry Trieu\Desktop\School\4650\Code\parking-citations.csv")
locationdf = locationdf["Location"].dropna()

#Get date
#for i in df:
 #   i = str(i)
  #  arrayDate.append(i[5:10])

#Get Year
#for i in df:
#    i = str(i)
#    arrayYear.append(i[:4])

#Get Month
#for i in df:
#    i = str(i)
#   arrayMonth.append(i[5:7])

#Get state
#for i in statedf:
#   i = str(i)
#    arrayState.append(i)

#Get location
for i in locationdf:
    i = str(i)
    arrayLocation.append(i)

#change the list to either arrayDate, arrayYear, or df
for i in locationdf:
    if i in map:
        map[i] = map[i]+1
    else:
        map[i] = 1

sortmap = sorted(map.items(), key = lambda kv: kv[1])
'''
x = []
y = []

for i,k in sortmap:
    x.append(int(i))
    y.append(int(k))
'''    
for i in sortmap:
    print(i)

