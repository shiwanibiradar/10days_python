#using break statement in program 
#to check the functionality of break
#

print("enter the number ")
a=int(input(""))
i=1
while i <= a:
	if i == 5:
		break
	print("prints number upto only 5 and they are",i)
	i +=1
