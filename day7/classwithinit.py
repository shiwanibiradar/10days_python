#program for class with init function 
#when we declared a class that time by defualt it calls init function(__init()__)

class Person:
  def __init__(self1, name, age):
    self1.name = name
    self1.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()



#self1 is a parameter which is reference to current instance of class 
#and it is used to access variables that belong to class
#you can use whatever word in placed of self 
