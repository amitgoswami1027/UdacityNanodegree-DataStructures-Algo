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

with open(r"C:\Users\agmak\Desktop\SVA\Desktop\AmitGoswami\DataStructureMasterReference\Project01\calls.csv", 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:" <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
def get_prefixes(phonenumber):
    if phonenumber[0] == "(":
       pos = phonenumber.find(")")
       prefix = phonenumber[1:pos]
       return prefix
    elif phonenumber[0] == "7" or phonenumber[0] == "8" or phonenumber[0] == "9":
       prefix = phonenumber[:4]
       return prefix
    else:
       prefix = phonenumber[0:3]
       return prefix

all_areacode_prefixes = []

for eachline in calls:
    caller_num = eachline[0]
    caller_prefix = caller_num[:5]
    
    if caller_prefix == "(080)":
       prefixes = get_prefixes(eachline[1])
       all_areacode_prefixes.append(prefixes)

all_areacode_prefixes = set(all_areacode_prefixes)

lexo_sort = []
for items in all_areacode_prefixes:
    lexo_sort.append(items)

lexo_sort.sort(key=str)

#PART-A: Print the answer as part of a message: "The numbers called by people in Bangalore have codes:" <list of codes>
print("The numbers called by people in Bangalore have codes")
for items in lexo_sort:
    print(items)

count1 = 0
count2 = 0

for eachline in calls: 
  if get_prefixes(eachline[0]) == "080":
     count1 += 1
  if get_prefixes(eachline[0]) == "080" and get_prefixes(eachline[1]) == "080":
     count2 += 1

percentage = (count2/count1) * 100

# PART B - Print the answer as a part of a message:: "<percentage> percent of calls from fixed lines in Bangalore are calls to other
# fixed lines in Bangalore." The percentage should have 2 decimal digits

print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
                                                        .format(str(round(percentage,2))))