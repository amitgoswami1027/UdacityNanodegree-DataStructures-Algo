import csv
import operator

"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

with open(r"C:\Users\agmak\Desktop\SVA\Desktop\AmitGoswami\DataStructureMasterReference\Project01\texts.csv", 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    #sort1 = sorted(texts, key=operator.itemgetter(2))

with open(r"C:\Users\agmak\Desktop\SVA\Desktop\AmitGoswami\DataStructureMasterReference\Project01\calls.csv", 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    call_sort = sorted(calls, key=operator.itemgetter(2))

"""
TASK 4:
The telephone company want to identify numbers that might be doing telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts, receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
outgoing_numbers = []
for eachline in calls:
    outgoing_numbers.append(eachline[0])

text_sending_numbers = []
for eachline in texts:
    text_sending_numbers.append(eachline[0])

outgoing_numbers = set(outgoing_numbers)
text_sending_numbers = set(text_sending_numbers)

telemarketer_numbers = outgoing_numbers.difference(text_sending_numbers)
print(text_sending_numbers)

print("These numbers could be telemarketers: ")
for items in text_sending_numbers:
    print(items)

