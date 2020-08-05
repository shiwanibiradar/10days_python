#program for prime number

i=1
while i <= 100:	
	count =0
	j=0
	while j < i:
		if i%j==0:
			count +=1
		i +=1
	if count <=0:
		print (i)
