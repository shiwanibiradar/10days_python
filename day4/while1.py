#Calculate the sum of digits of a number given by user.



num=int(input("ENTER THE NUMBER THAT YOU WANT TO ADD\n"))
result=0
while num > 0:
	r = num % 10
	result = result+r
	num = int(num /10)
print(result)

