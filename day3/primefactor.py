#program for prime factor 



num=int(input("Enter the number"))
for i in range(2,num+1):
        if (num % i==0):
                prime=1
                for j in range(2,(i//2+1)):
                        if (i %j==0):
                                prime=0
                                break
                if (prime==1):
                        print("%d is a prime factor of a given no %d"%(i,num))
