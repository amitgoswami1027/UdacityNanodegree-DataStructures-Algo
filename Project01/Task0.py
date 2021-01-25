import csv
import operator

"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
Explicitly putting "r" before the string and it is not a typo :). Its actually means raws input string in Python. 
otherwise it will flash the error.
"""

with open(r"C:\Users\agmak\Desktop\SVA\Desktop\AmitGoswami\DataStructureMasterReference\Project01\texts.csv", 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    sort1 = sorted(texts, key=operator.itemgetter(2))

with open(r"C:\Users\agmak\Desktop\SVA\Desktop\AmitGoswami\DataStructureMasterReference\Project01\calls.csv", 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    sort2 = sorted(calls, key=operator.itemgetter(2))

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
#print(sort1)
print ("First record of texts, " + str(sort1[0][0]) + " texts " + str(sort1[0][1]) + " at time " + str(sort1[0][2]) )
print ("First record of texts, " + str(sort1[-1][0]) + " texts " + str(sort1[-1][1]) + " at time " + str(sort1[-1][2]) )




