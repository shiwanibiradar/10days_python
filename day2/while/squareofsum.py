#Write a Program for sqaure of sum of n numbers

num=int(input("Enter the numbers"))
sm=0
for i in range(1,num+1):
	sm = sm+i
sm=pow(sm,2)
	
print(sm)
