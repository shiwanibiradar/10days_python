#A three digit number is called Armstrong number if sum of cube of its digit is equal to number itself.
#E.g.- 153 is an Armstrong number because (13)+(53)+(33) = 153.
#Write all Armstrong numbers between 100 to 500.

a=[]
num=100
result=0
while num <= 500: 
	r= num %10
	num1= int(num/10)
	num2=num1%10
	num3=int(num1/10)
	result=(num3*num3*num3)+(num2*num2*num2)+(r*r*r)
	if num == result:		
		a.append(result)
	num = num+1
print(a)
