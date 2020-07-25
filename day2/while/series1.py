#print 101010 in pattern of 
#1010101
# 10101
#  101


i=1
j=2
while i >=1:
	a= " "*j+"*"*i+" "*j
	print (a)
	i = i+2
	j = j-1
	if i> 5:
		break

