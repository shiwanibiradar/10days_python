#program for continue statement
#continue statement will stop current itteration and will go with 
#next itteration
#this program will run no upto a except 3

print("enter the number")
a=int(input(""))
i=0
while i < a:
	i +=1
	if i == 3:
		continue
	print(i)
