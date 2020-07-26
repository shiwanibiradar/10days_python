#creating a list for names of girls

mylist=["shiwani","shraddha","snehal","sanyukta","tejaswini"]
print(mylist)
print(mylist[0])
print(mylist[1])

#negative indexing
print(mylist[-1])
print(mylist[-2])

#range of indexing in lists
print(mylist[2:7])

#another example of range
print(mylist[:3])
#(will print output upto 2nd indexing

print(mylist[2:])
#(will print from 3rd indexing)

#change item index
mylist[1]="rohan"
print(mylist)

#check whether particular name is present in list or not
if "shiwani" in mylist:
	print("yes, she is in list")


#print length of lists
print(len(mylist))

#add item in list
mylist.append("ravi")
print(mylist)

#insert any item at particular index
mylist.insert(1,"govind")
print(mylist)
#(name which is before at 1 index will go on 2nd automatically)

#add 2 lists 
list1=["grapes","appple","watermelon"]
list2=["mango","chickoo"]
list3=list1+list2
print(list3)

