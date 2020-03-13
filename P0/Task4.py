"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

tel_nos = set()
non_tel_nos = set()
counter = 0
for i in calls:
    tel_nos.add(i[0])
    non_tel_nos.add(i[1])
    counter+=1
for j in texts:
    non_tel_nos.add(j[0])
    non_tel_nos.add(j[1])

tel_nos = tel_nos - non_tel_nos
print("These numbers could be telemarketers: ")
for elem in sorted(tel_nos):
    print(elem)


"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

