import csv
import operator

"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
Explicitly putting "r" before the string and it is not a typo :). Its actually means raws input string in Python. 
otherwise it will flash the error.
Review Suggesion: No need to sort as the lists are already sorted.
"""

with open(r"C:\Users\agmak\Desktop\SVA\Desktop\AmitGoswami\DataStructureMasterReference\Project01\texts.csv", 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    
with open(r"C:\Users\agmak\Desktop\SVA\Desktop\AmitGoswami\DataStructureMasterReference\Project01\calls.csv", 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    
"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

print("First record of texts, {} texts {} at time {}"
            .format(texts[0][0], texts[0][1], texts[0][2]))
print("Last record of calls, {} calls {} at time {}, lasting {} seconds"
            .format(calls[-1][0], calls[-1][1], calls[-1][2], calls[-1][3]))
