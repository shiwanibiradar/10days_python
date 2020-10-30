#take no of student
#firstly name and marks of subjects
#then create query and using query you have to find the average marks of this query
#inputs : 
#no of students
# name and marks 
#and query name means name of student for average marks

n=int(input("Enter the number of student"))
d={}
for i in range(n):
	name, *line = input().split()
	marks = list(map(float, line))
	d[name]=marks
query_name=input("enter the query")
#print(s)
#list=list(set(s))
#print(list)
total_marks= sum(d[query_name])
average_marks= total_marks/3
print("%.2f"%(average_marks))
