#program for factorial of given number

i=1
fact=1
print("enter the number")
n=int(input())
while i <= n:
	fact=fact*i
	print('factorials are',fact)
	i +=1
