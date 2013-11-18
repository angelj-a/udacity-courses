#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment


import sys

salesSubTotal = 0
count = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
	salesSubTotal += float(cost)
	count += int(1)

print "{0}\t{1}".format(count, salesSubTotal)

