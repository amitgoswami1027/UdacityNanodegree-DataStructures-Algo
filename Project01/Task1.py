import csv

"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

with open(r"C:\Users\agmak\Desktop\SVA\Desktop\AmitGoswami\DataStructureMasterReference\Project01\texts.csv", 'r') as f:
    reader = csv.reader(f)
    textslist = list(reader)

with open(r"C:\Users\agmak\Desktop\SVA\Desktop\AmitGoswami\DataStructureMasterReference\Project01\calls.csv", 'r') as f:
    reader = csv.reader(f)
    callslist = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message: "There are <count> different telephone numbers in the records."
"""

unique_text_numbers = set()
for eachline in textslist:
    unique_text_numbers.add(eachline[0])
    unique_text_numbers.add(eachline[1])

unique_calls_numbers = set()
for eachline in callslist:
    unique_calls_numbers.add(eachline[0])
    unique_calls_numbers.add(eachline[1])

phone_numbers = unique_calls_numbers.union(unique_text_numbers)

total_diff_tel_number = len(phone_numbers)

# Print Message - "There are <count> different telephone numbers in the records."
print("There are {} different telephone numbers in the records"
                            .format(str(total_diff_tel_number)))
