#give input from yser and print second largest numbers 
n= int(input())
arr=map(int,input().split())
largest=secondlatest= -101
for x in arr:
	if x > largest:
		tmp=largest
		largest=x
		secondlargest=tmp
	elif x > secondlargest and x !=largest:
		secondlatest=x
print(secondlargest)
