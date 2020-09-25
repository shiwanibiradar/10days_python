#example for re package
#declare a string and find first word n last word
import re
#str='this is my first example'
#match = re.search(r'example',str)
#if match:
#	print("found"), match.group()
#else:
#	print("did not found")

match1=re.search(r'\w\s*\w\s*\w','xx1 2    3xx')
print("found",match1.group())
