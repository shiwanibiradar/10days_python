#A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
#Ask user for quantity
#Suppose, one unit will cost 100.
#Judge and print total cost for user

quantity=int(input("enter the quantity"))
if(quantity * 100 > 1000):
	print("final price with discount",((quantity * 100)-(.1*quantity *100)))
else:
	print("final cost is",quantity*100)

