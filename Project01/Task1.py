import csv

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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# Adding all the phone numbers in the list from the text csv file.
text_list_numbers = []
for eachline in texts:
    text_list_numbers.append(eachline[0])
    text_list_numbers.append(eachline[1])

# Adding all the phone numbers in the list from the calls csv file.
calls_list_numbers = []
for eachline in calls:
    calls_list_numbers.append(eachline[0])
    calls_list_numbers.append(eachline[1])

# Converting List to Sets for making sure all numbers are unique.
text_set = set(text_list_numbers)
calls_set = set(calls_list_numbers)

# Union of both the above list will give the total unique phone numbers. 
different_tel_number = calls_set.union(text_set)

total_diff_tel_number = len(different_tel_number)

print(different_tel_number)
print(total_diff_tel_number)

# Print Message - "There are <count> different telephone numbers in the records."
print ("There are " + str(total_diff_tel_number)) + "different telephone numbers in the records.")
