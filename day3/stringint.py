#From a list containing ints, strings and floats, make three lists to store them separately

a=[2,"shiwani",2.230]
x=[]
y=[]
z=[]
for i in a:
	if type(i) == int:
		x.append(i)
	if type(i) == float:
		z.append(i)
	if type(i) == str:
		y.append(i)
print("int value is ",x)
print("string value is ",y)
print("string value is ",z)

