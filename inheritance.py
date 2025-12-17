# Inheritance is code resulabilty

# Single Level inheritance

class dad:              # parent class
    def house(self):
        print("im from dad property")
class son(dad):         # child class
    def factory(self):
        print("im from son property")
s1=son()
s1.house()
s1.factory()

# V1 override function 

class app1:
    def v1(self):
        print("orders")
class app1_1(app1):
    def v2(self):
        print("return")
    def v1(self):         
        print("refund")

a=app1_1()
a.v1()
a.v2()

# MultiLevel Inheritance

class ford:
    def model1(self):
        print("Ford first model")
class mustang(ford):
    def model2(self):
        print("mustang is second model of ford")
class person(mustang):
    def driver(self):
        print("IM the driver drive all car")

dr=person()
dr.driver()
dr.model1()
dr.model2()

# Heriarchial inhertiance ( Sub classes using parent class only )

class redmi:
    def mi(self):
        print("snapdragon processor")
class poco(redmi):
    def x3(self):
        print("gaming phone")
class xioami(redmi):
    def c3(self):
        print("camera quality")

phone=poco()
phone.x3()
phone.mi()

phone1=xioami()
phone1.c3()
phone1.mi()

# Multiple Inheritance

class ktm:
    def duke(self):
        print("i have a duke bike")
class yamaha:
    def mt(self):
        print("i have a mt bike")
class rider(yamaha,ktm):     # sub class using two parent class
    def riding(self):
        print("i ride the all bike")
r1=rider()
r1.duke()
r1.mt()
r1.riding()


