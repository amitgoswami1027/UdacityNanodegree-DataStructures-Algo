import csv
import operator

"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""

with open(r"C:\Users\agmak\Desktop\SVA\Desktop\AmitGoswami\DataStructureMasterReference\Project01\texts.csv", 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    
with open(r"C:\Users\agmak\Desktop\SVA\Desktop\AmitGoswami\DataStructureMasterReference\Project01\calls.csv", 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    call_sort = sorted(calls, key=operator.itemgetter(2))


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
#Print a message:
#"<telephone number> spent the longest time, <total time> seconds, on the phone during September 2016."
print( str(call_sort[-1][0]) + "spent the longest time, " + str(call_sort[-1][3]) + " seconds, on the phone during spetember 2016")


