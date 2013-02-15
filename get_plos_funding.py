# Description: This script scrapes funding text from PLOS journal articles using a list of PLOS doi URLs as input. It assumes that the funding paragraph begins with the keyword "Funding:" Takes a CSV listing URLs as input. Outputs a CSV listing funding data.
# Requirements: Python 2.5, BeautifulSoup
# Usage: python get_plos_funding.py input_path output_path
# Input: must be a CSV listing URLs in first column
# Contact: Russell White, russellwhite@gmail.com

import urllib2
import re
from BeautifulSoup import BeautifulSoup
import csv
import sys

input_path = sys.argv[1]
output_path = sys.argv[2]

output = csv.writer(open('/Users/bridgetgrady/Desktop/PYTHON/plos_output2.csv','w'),delimiter=',',quoting=csv.QUOTE_ALL

urls = csv.reader(open(input_path,'rU'))
number = 0
safelist = ['The funders had no role','no support','no funding']


for row in urls:
	number += 1
	print 'We are on row ' + str(number)
	try:
		urlx = row[0]
		print 'the doi is ' + urlx
		usock = urllib2.urlopen(urlx)
		soup = BeautifulSoup(usock)
		funding_paragraph = soup.find(text=re.compile('Funding:'))
		print funding_paragraph
		parent = funding_paragraph.parent
		print parent
		grandparent = parent.parent
		str_grandparent=str(grandparent)
		print str_grandparent
		for item in safelist:
			if str_grandparent.find(item) != -1:
				print item + ' found in paragraph, condidering verified.'
				verify_key = 'yes'
				break
			else:
				verify_key = 'no'
				print 'keywords not found in paragraph.  Verify.'	
	except AttributeError:
		grandparent = 'ERROR RETRIEVING DATA'
	data = [urlx,grandparent,verify_key]
	output.writerow(data)
usock.close()