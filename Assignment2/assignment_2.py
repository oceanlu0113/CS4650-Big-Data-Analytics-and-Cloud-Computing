# -*- coding: utf-8 -*-
"""Assignment #2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dbBDkfrQgQiU9DKWKjeF6V36iFM5XDcA
"""

# 1.	Read in the data set.
# Upload csv file 'City_Employee_Salaries_March_2018.csv'

from google.colab import files
uploaded = files.upload()

# 2.	Display the first 50 data entries/rows as well as last 50 entries/rows.

import pandas as pd
pd.set_option("display.max_columns",9)
pd.set_option("display.width",1000)

df = pandas.read_csv('City_Employee_Salaries_March_2018.csv', index_col='Name')
df.head(50)

# 3.	Display a quick statistical information on all numerical columns such as count, mean, std, min, max, etc. 

Annual_Rt_Count = df['Annual_Rt'].count()
Annual_Rt_Mean = df['Annual_Rt'].mean()
Annual_Rt_Std = df['Annual_Rt'].std()
Annual_Rt_Min = df['Annual_Rt'].min()
Annual_Rt_Max = df['Annual_Rt'].max()
print ('Annual_Rt Count: ' + str(Annual_Rt_Count))
print ('Annual_Rt Mean: ' + str(Annual_Rt_Mean))
print ('Annual_Rt Std: ' + str(Annual_Rt_Std))
print ('Annual_Rt Min: ' + str(Annual_Rt_Min))
print ('Annual_Rt Max: ' + str(Annual_Rt_Max))

Hrly_Rate_Count = df['Hrly_Rate'].count()
Hrly_Rate_Mean = df['Hrly_Rate'].mean()
Hrly_Rate_Std = df['Hrly_Rate'].std()
Hrly_Rate_Min = df['Hrly_Rate'].min()
Hrly_Rate_Max = df['Hrly_Rate'].max()
print ('\nHrly_Rate Count: ' + str(Hrly_Rate_Count))
print ('Hrly_Rate Mean: ' + str(Hrly_Rate_Mean))
print ('Hrly_Rate Std: ' + str(Hrly_Rate_Std))
print ('Hrly_Rate Min: ' + str(Hrly_Rate_Min))
print ('Hrly_Rate Max: ' + str(Hrly_Rate_Max))

# 4.	Select a subset of rows (you decide which subset to select or which criteria to use for selection.) Display the first 10 data entries selected.
# subset of rows is from 500-1000, printing top 10 would be 500-510

subsetRows = df[500:1000]
print(subsetRows.head(10))

# 5.	Similar to 4, but select a subset of columns (from original data). Display the first 10 data entries with selected columns.
# subset of columns is from "Job_Title"

subsetCol = df["Job_Title"]
print(subsetCol.head(10))

# 6.	From original data, filter out some data, for example, filter out those salary lower than certain amount. After filtering out the data, display the first 50 data entries. 
# Filter those who make above 70,000 or lower per hour in the column "Annual_Rt"

middleClass = df[df['Annual_Rt'] <= 70000]
print(middleClass.head(50))

# 7.	From original data, find out all entries with missing values. Display the first 10 entries.

missingValues = df[df.isna().any(axis=1)]
print (missingValues)

# 8.	Manipulate the original data by changing numerical values of specific column(s) (for example, give everyone 10% raise!) Display the first 10 entries before update and after update.
# gave everyone a 10% raise

raiseSalary = pandas.read_csv('City_Employee_Salaries_March_2018.csv', index_col='Name')
raiseSalary.Annual_Rt = raiseSalary.Annual_Rt*1.1
print (raiseSalary.head(10))

# 9.	Sort the data set resulted from step 8 in certain way (e.g.  descending order of salaries)
# descending order of Dept

sortedSalary = raiseSalary.sort_values('Dept', ascending=True)
print (sortedSalary.head(10))

# 10.	Group the data set from step 9 based on certain category (e.g. group based on rank of Professor, Assoc Professor, etc.)
# showing group based on rank of Job_Title

grouped = sortedSalary.groupby('Job_Title').mean()
print (grouped.head(20))

# 11.	(optional) Plot data (or subset of data) in at least three different ways such as vertical bar graph, horizontal bar graph, curve, … 

df.plot(x = 'FID', y = "Annual_Rt", kind = 'scatter')