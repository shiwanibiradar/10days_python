#check whether given no is pallindrome or not


num=(input())
rev=0
temp=num
while num:
	dig=num%10
	rev=rev*10+dig
	num=num//10
if temp==rev:
	print("It is pallindrome")
else:
	print("its not")
	
