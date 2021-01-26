import csv
import operator
import random

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
    #call_sort = sorted(calls, key=operator.itemgetter(2))

"""
TASK 3:(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start with the area code 140.

Part B: What percentage of calls from fixed lines in Bangalore are made to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
#PART-A : Function to get prefixes from the phone number.
def get_prefixes(phonenumber):
    # Fixed Line area codes enclosed in brackets
    #print(phonenumber)
    if phonenumber[0] == "(":
       pos = phonenumber.find(")")
       prefix = phonenumber[1:pos]
       return prefix
    elif phonenumber[0] == "7" or phonenumber[0] == "8" or phonenumber[0] == "9":
       prefix = phonenumber[1:5]
       return prefix
    else:
       prefix = phonenumber[0:3]
       return prefix

startloc=1
endloc=4
bang_prefix = '080'

#PART-A: Fetching all the Phone Number prefixes and store in the "called_codes" list in Bangalore.
called_codes = []
for eachline in calls:
    caller_num = eachline[0]
    caller_prefix = caller_num[1:4]
    if caller_prefix == bang_prefix:
       prefixes=get_prefixes(eachline[1])
       called_codes.append(prefixes)

#PART-A: Print the answer as part of a message:
#"The numbers called by people in Bangalore have codes:<list of codes>
#The list of codes should be print out one per line in lexicographic order with no duplicates.

called_codes = set(called_codes)

lexo_sort = []
for items in called_codes:
    lexo_sort.append(items)

lexo_sort.sort(key=str)

#PART-A: The list of codes should print out one per line in lexicographic order with no duplicates
print("The list of codes should print out one per line in lexicographic order with no duplicates")
for items in lexo_sort:
    print(items)

"""
Part B: What percentage of calls from fixed lines in Bangalore are made to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls were made to a number also starting with "(080)"?

Print the answer as a part of a message:: "<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore." The percentage should have 2 decimal digits
"""

total_num_calles = len(calls)
print(total_num_calles)

called_bangalore_codes = []
for eachline in calls:
    caller_num = eachline[0]
    caller_prefix = caller_num[startloc:endloc]
    called_num = eachline[1]
    called_prefix = called_num[startloc:endloc]
    if caller_prefix == called_prefix:
       called_bangalore_codes.append(eachline[1])

total_bangalore_calls = len(called_bangalore_codes)
print(total_bangalore_calls)

#PART-B
percentage = (total_bangalore_calls/total_num_calles)*100

print( str(round(percentage,2)) + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
