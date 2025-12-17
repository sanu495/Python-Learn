# polymorphism

# we can't overloading in function

class dad:
    def house(self):
        print("yellow house")
class daugther(dad):
    def factory(self):
        print("white factory")
    def house(self):          # we can overwrite the function is polymorphism
        print("red house")    # Not possible to pass the arguments in function

user=daugther()
user.factory()
user.house()