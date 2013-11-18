#!/usr/bin/python

import sys
from collections import defaultdict

hitsPerPage = defaultdict(int)

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisResource, thisHits = data_mapped

    hitsPerPage[thisResource] += int(thisHits)

for key,count in hitsPerPage.items():
    print "{0}\t{1}".format(key,count)
