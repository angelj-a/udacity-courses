import re
import parserCLF
import unittest



class ParserCLFTestCase(unittest.TestCase):
	
	def test_parseLineMatches(self):
		line = """10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /displaytitle.php?id=347 HTTP/1.1" 200 10469"""
		
		expected_ip = "10.223.157.186"
		expected_id = "-"
		expected_uname = "-"
		expected_timef = "[15/Jul/2009:15:50:35 -0700]"
		expected_requestline = "GET /displaytitle.php?id=347 HTTP/1.1"
		expected_statuscode = "200"
		expected_size = "10469"
		
		res = parserCLF.parseLine(line)
		
		self.assertNotEqual(res,None)
		self.assertEqual(expected_ip,res[0])
		self.assertEqual(expected_id,res[1])
		self.assertEqual(expected_uname,res[2])
		self.assertEqual(expected_timef,res[3])
		self.assertEqual(expected_requestline,res[4])
		self.assertEqual(expected_statuscode,res[5])
		self.assertEqual(expected_size,res[6])	
		
	def test_getResourceNameMatches(self):
		req = "GET /displaytitle.php?id=347 HTTP/1.1"
		
		expected_resource = "/displaytitle.php?id=347"
		res = parserCLF.getResourceName(req)
		
		self.assertNotEqual(res,None)
		self.assertEqual(expected_resource,res)
		

if __name__ == '__main__':
    unittest.main()
