# class and object

class Student:
    def user(self):      # self is used for which object is using class clarification
        print("hi im a student")
s1=Student()
s1.user()

# class with multiple object

class Teacher:
    def __init__(self, name, subject):
        self.name=name
        self.subject=subject
    def school(self):
        print(f"The Teacher {self.name} is taking a {self.subject} subject")

t1=Teacher("maria","Maths")
t1.school()
t2=Teacher("antony","English")
t2.school()
t3=Teacher("Grabila","Science")
t3.school()

# Constructor

class Employee:
    def __init__(self,Name,Aadhar_num):
        self.x=Name
        self.y=Aadhar_num
    def enter_office(self):
        print(f"{self.x} enters office using Aadhar number {self.y}")

    def bank_account(self):
        print(f"Bank account is opened for {self.x} using with Aadhar number {self.y}")

emp1=Employee("Sanoop","4558489493938")
emp1.enter_office()
emp1.bank_account()

emp2=Employee("Sebina","88595947383677")
emp2.enter_office()
emp2.bank_account()


# With out Constructor

class math:
    def square(self,n):
        return n * n
    def cube(self,n):
        return n * n * n

cal=math()
print(cal.square(5))
print(cal.cube(5))
tool=math()
print(tool.cube(6))
print(tool.square(6))