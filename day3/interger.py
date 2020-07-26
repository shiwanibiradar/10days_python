#You are given with a list of integer elements. 
#Make a new list which will store square of elements of previous #list.

numberlist=[2,3,4,5]
ls=[]
for x in numberlist:
	ls.append(x ** 2)
print(ls)
