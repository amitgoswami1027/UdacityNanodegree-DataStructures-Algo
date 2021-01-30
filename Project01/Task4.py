import csv
import operator

"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

with open(r"C:\Users\agmak\Desktop\SVA\Desktop\AmitGoswami\DataStructureMasterReference\Project01\texts.csv", 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    
with open(r"C:\Users\agmak\Desktop\SVA\Desktop\AmitGoswami\DataStructureMasterReference\Project01\calls.csv", 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
 
"""
TASK 4:
The telephone company want to identify numbers that might be doing telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts, receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

callers_set = set()
called_set = set()

for eachline in calls:
    callers_set.add(eachline[0])
    called_set.add(eachline[1])

texters_set = set()
texted_set =set()

for eachline in texts:
    texters_set.add(eachline[0])
    texted_set.add(eachline[1])

telemarketer_numbers = callers_set.difference(called_set).difference(texters_set).difference(texted_set)

print("These numbers could be telemarketers: ")
for items in sorted(telemarketer_numbers):
    print(items)

