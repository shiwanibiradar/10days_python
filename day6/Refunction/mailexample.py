#suppose you want to search mail id inside string 'zyx abc@gmail.com monkry'

import re
n=int(input())
for i in range(n):
	str1=input()
#match = re.search(r'\w@\w+',str)
	match = re.match(r'[\w.-]+@+[\w.-]+',str1)
print(str1)
for i in str1:
	if match:
		print("Valid mail")
		break
	else:
		print("Invalid mail")
		break
