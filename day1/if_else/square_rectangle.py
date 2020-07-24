#Take values of length and breadth of a rectangle from user and check if it is square or not.


length=int(input("Enter the length"))
breadth=int(input("Enter the breadth"))
if(length==breadth):
	value1= length*breadth
	print("It is Square with Area ", value1)
elif(length != breadth):
	value2= length *breadth
	print("It is rectangle with Area", value2)

