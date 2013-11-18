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
		req = matches.groups()[0]
		o = urlparse(req)
		# According to udacity forum:
		# res = o.path + o.params + o.query
		res = o.path
		if o.params:
			res += ";" + o.params
		if o.query:
			res += "?" + o.query
	except:
		res = None
	return res

