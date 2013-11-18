#!/usr/bin/python

import sys
from collections import defaultdict

hitsPerIP = defaultdict(int)

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisIP, thisHits = data_mapped

    hitsPerIP[thisIP] += int(thisHits)

for key,count in hitsPerIP.items():
    print "{0}\t{1}".format(key,count)
