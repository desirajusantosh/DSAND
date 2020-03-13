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
for i in calls:
    tel_nos.add(i[0])
    tel_nos.add(i[1])
for j in texts:
    tel_nos.add(j[0])
    tel_nos.add(j[1])
print("There are "+str(len(tel_nos))+" different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
