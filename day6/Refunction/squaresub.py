#sampal example for sub string i.e re.sub() function


import re
def square(match):
	number=int(match.group())
	return str(number**2)
print (re.sub(r'\d+',square,"1,2,3,4,5,6,7,8"))
