#Using range(1,101), make two list, 
#one containing all even numbers and other containing all odd numbers.

a=[]
b=[]
for i in range(1,101):
	if i%2 ==0:
		a.append(i)
	else:
		b.append(i)
print("even number list is ",a)
print("\n")
print("odd numbers list is",b)			

#From the two list obtained in previous question, 
#make new lists, containing only numbers 
#which are divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.
c=[]
d=[]
e=[]
f=[]
for i in a:
	if i%4==0:
		c.append(i)
	if i%6==0:
		d.append(i)
	if i%8==0:
		e.append(i)
	if i%10==0:
		f.append(i)
print("\nThe numbers which are divisible by 4 are",c)
print("\nThe numbers which are divisible by 6 are",d)
print("\nThe numbers which are divisible by 8 are",e)
print("\nThe numbers which are divisible by 10 are",f)
g=[]
h=[]
j=[]
k=[]
for i in b:
	if i%3==0:
		g.append(i)
	if i%5==0:
		h.append(i)
	if i%7==0:
		j.append(i)
	if i%9==0:
		k.append(i)
print("\nThe numbers which are divisible by 3 are",g)
print("\nThe numbers which are divisible by 5 are",h)
print("\nThe numbers which are divisible by 7 are",j)
print("\nThe numbers which are divisible by 9 are",k)
