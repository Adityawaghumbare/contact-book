class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old")

class Student:
    def __init__(self,name,r_no,age):
        self.name = name
        self.r_no = r_no
        self.age =age

    def show_details(self):
        print(f"Name : {self.name} \nRoll noumber : {self.r_no}\nAge = {self.age}")

x = input("Enter your name : ")
y = int(input("Enter your age : "))
p1 = Person(x,y)
p1.greet()



s1 = Student(x,65,y)
s1.show_details()

s2 = Student("Piyush",35,19)
s2.show_details()