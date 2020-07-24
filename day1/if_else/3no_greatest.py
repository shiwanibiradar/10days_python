#3no are there and find greatest no from 3 no 

no1=int(input("Enter the no1 "))
no2=int(input("Enter the no2 "))
no3=int(input("Enter the no3 "))
if (no1 > no2) & (no1 > no3):
	largest=no1
elif(no2 > no3) & (no2 > no1):
	largest=no2
else:
	largest=no3
print("largest no is", largest)
