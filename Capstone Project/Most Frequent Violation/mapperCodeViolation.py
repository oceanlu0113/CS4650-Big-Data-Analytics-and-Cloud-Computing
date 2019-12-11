#mapper 
#!/usr/bin/python
import sys 

for line in sys.stdin:
    line.strip();
    line = line.strip(",")
    if len(line) >= 2:
        ##set a variable to equal values in a column
        violationCode = line[15]
        #print out the inupt with the value of 1
        print("%s\t%s"% (violationCode,1))