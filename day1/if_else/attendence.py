#A student will not be allowed to sit in exam if his/her attendence is less than 75%.
#Take following input from user
#Number of classes held
#Number of classes attended.
#And print
#percentage of class attended
#Is student is allowed to sit in exam or not.

lec=int(input("Enter the no of lectures"))
attended=int(input("Enter the no of attended"))
percentage= attended / lec * 100\

if(percentage > 75):
	print("Allow to sit in exam ")
else:
	print("Not allow to sit in exam") 
