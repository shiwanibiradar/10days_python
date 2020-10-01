#check given mobile numbers are valid or not

import re
num=input()
num1=len(str(num))
print (num1)
if num1 ==10:
	match=re.search(r'^[789]\d',num)
	print("number is valid")
else:
	print("no is not valid")

