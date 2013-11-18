#!/usr/bin/python

# Format of each line is in Common Log Format


import sys
from collections import defaultdict
import re
from urlparse import urlparse

patternCLF = re.compile(r"""^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(-|\w+)\s+(-|\w+)\s+(\[.*\])\s+\"(.*)\"\s+(\d{3})\s+(-|\d+)\s*$""")
patternReq = re.compile(r"""^[A-Z]+\s+(.*)\s+.*$""")


def parseLine(s):
	matches = patternCLF.match(s)
	try:
		res = matches.groups()
	except:
		res = None
	return res
	
def getResourceName(s):
	matches = patternReq.match(s)
	try:
		res = matches.groups()[0]
		o = urlparse(req)
		#According to udacity forum:
		res = o.path + o.params + o.query
	except:
		res = None
	return res

hitsPerPage = defaultdict(int)

for line in sys.stdin:
    data = parseLine(line)
    if data and len(data) == 7:
        ip, iden, uname, time, req, code, size = data
        hitsPerPage[getResourceName(req)] += 1

for key,count in hitsPerPage.items():
    print "{0}\t{1}".format(key,count)


