#you have given string
#then search for string which you have to found in given strring
#then print index of that string

n=input()
n1=input()
import re
match=re.compile(n1)
r = match.search(n)
if not r:
	print ((-1,-1))
while r:
	print("({0},{1})".format(r.start(),r.end() -1))
	r= match.search(n,r.start()+1)
