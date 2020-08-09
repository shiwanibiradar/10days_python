def shiwani(number):
        total = 0
        for x in number:
                total = total+int(x)
        return total
a=[]
print("Enter the how many numbers you want to add in lists")
num=int(input())
i=0
while i < num:
	b=input("Enter the number in lists")
	a.append(b)
	i +=1
print("lists of numbers is",a)
print("addition of numbers in lists is",shiwani((a)))

