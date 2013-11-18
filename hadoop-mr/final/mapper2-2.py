#!/usr/bin/python

# Format of each line is in Common Log Format

import sys
from collections import defaultdict
import re
from urlparse import urlparse

patternCLF = re.compile(r"""^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(-|\w+)\s+(-|\w+)\s+(\[.*\])\s+\"(.*)\"\s+(\d{3})\s+(-|\d+)\s*$""")

def parseLine(s):
	matches = patternCLF.match(s)
	try:
		res = matches.groups()
	except:
		res = None
	return res
	
hitsPerIP = defaultdict(int)

for line in sys.stdin:
    data = parseLine(line)
    if data and len(data) == 7:
        ip, iden, uname, time, req, code, size = data
        hitsPerIP[ip] += 1

for key,count in hitsPerIP.items():
    print "{0}\t{1}".format(key,count)


