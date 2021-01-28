import csv
import operator
import collections

"""
Read file into calls.
"""
with open(r"C:\Users\agmak\Desktop\SVA\Desktop\AmitGoswami\DataStructureMasterReference\Project01\calls.csv", 'r') as f:
    reader = csv.reader(f)
    callslist = list(reader)
    #call_sort = sorted(calls, key=operator.itemgetter(2))

"""
TASK 2: Which telephone number spent the longest time on the phone during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message: "<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".

So, your code should add up the time for numbers that both made the call and received it.
For example, if xxx made a call to yyy for 5 min and then xxx received a call for 3 min then xxx was on the phone for 8 min.
"""

phone_dict= dict()

for eachline in callslist:
    if eachline[0] in phone_dict:
        phone_dict[eachline[0]] = phone_dict[eachline[0]] + eachline[3]
    if eachline[1] in phone_dict:
        phone_dict[eachline[1]] = phone_dict[eachline[1]] + eachline[3]
    phone_dict[eachline[0]] = eachline[3]

print(phone_dict)

#Print a message:
#"<telephone number> spent the longest time, <total time> seconds, on the phone during September 2016."
#print( str(call_sort[-1][0]) + "spent the longest time, " + str(call_sort[-1][3]) + " seconds, on the phone during spetember 2016")


#print("There are {} different telephone numbers in the records"
#                            .format(str(total_diff_tel_number)))