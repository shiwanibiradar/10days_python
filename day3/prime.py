#Using range(1,101), make a list containing only prime numbers.

a=[]
for i in range(1,102):
	for j in range(2,i-1):
        	if i%j==0: break
	else:
		if i > 1:
			a.append(i)
print(a)
