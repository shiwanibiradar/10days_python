#Create a Student class and initialize it with name and roll number. Make methods to :
#1. Display - It should display all informations of the student.
#2. setAge - It should assign age to student
#3. setMarks - It should assign marks to the student.

class student:
	def __init__(self,name,roll):
		self.name=name
		self.roll=roll
	def display(self):
		print(self.name)
		print(self.roll)
	def setage(self,age):
		self.age=age
	def setmarks(self,marks):
		self.marks=marks
b=student("shiwani",12)
b.display()
