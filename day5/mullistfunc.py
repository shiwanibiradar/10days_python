#Multiply the number in a list using function

def multiplication(number):
	total=1
	for x in number:
		total = total * int(x)
	return total

print("Enter how many no you want in list")
num=int(input(""))
i=0
b=[]
while i < num:
	a=input("Enter the number in list")
	b.append(a)
	i +=1
print("numbers in list are ", b)
print("multiplication of numbers of lists are",multiplication((b)))
