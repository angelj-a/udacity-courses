#!/usr/bin/python

import sys

salesTotal = 0
numberOfSales = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisNumSales, thisSale = data_mapped

    salesTotal += float(thisSale)
    numberOfSales += float(thisNumSales)
	

print numberOfSales, "\t", salesTotal

