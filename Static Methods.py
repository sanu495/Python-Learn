 # Instance & Class method & Static Method

class My_class:
    def instance(self):
        print("Im a normal instance method")

    @classmethod                             # class method
    def class_method(cls):
        print("Im from class Method")

    @staticmethod                            # static method
    def static_method():
        print("Im from static method")

obj=My_class()
obj.instance()

My_class.class_method()                     # Don't need to create a obj to call class method
My_class.static_method()                    # Don't need to create a obj to call static method

    
# class method

class Employee:
    company_name="OPEN AI"        # In the class method we can override the class level variable value

    @classmethod
    def change_name(cls,new_name):
        cls.company_name=new_name

# Static Method

    @staticmethod
    def alter_change_name(another_name):
        company=another_name

Employee.change_name("Google")   # overwrite the company name
print(Employee.company_name)

Employee.alter_change_name("Meta")  # Unable to control the class variable 
print(Employee.company_name)



# static method

class cal:

    @staticmethod                 # In static method we can't override already defined value
    def add(a,b):                 # Not possible to change a class level data and object level data
        return a + b

print(cal.add(34,7)) 







