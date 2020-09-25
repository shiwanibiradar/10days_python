#suppose you want to search mail id inside string 'zyx abc@gmail.com monkry'

import re
str="purpul abc@gmail.com monkey"
#match = re.search(r'\w@\w+',str)
match = re.search(r'[\w.-]+@+[\w.-]+',str)
if match:
	print("found",match.group())
else:
	print("did not match")
