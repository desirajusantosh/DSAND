"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import operator
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

d = {}
j = 0
for i in calls:
    if i[0] not in d.keys():
        d[i[0]] = int(i[3])
    else:
        d[i[0]] += int(i[3])
    if i[1] not in d.keys():
        d[i[1]] = int(i[3])
    else:
        d[i[1]] += int(i[3])

itemMaxCallDuring = max(d.items(), key=lambda x: x[1])
print(itemMaxCallDuring[0]+" spent the longest time, " + str(itemMaxCallDuring[1]) + " seconds, on the phone during September 2016.")
#print(max(d.items(), key=operator.itemgetter(1))[0])
"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

