# Access Specifier

# Access Specifiers for variables.abs

class parent:
    def __init__(self):
        self.Public_var="Im from Public"
        self._Protected_var="Im from Protected"    # Protected variable  (access: Sub class and Stranger class)
        self.__Private_var="Im from Private"       # Private Variable    (access: No access to any class except parent class)

    def access_same(self):
        print("The Parent class access")
        print("Public -> ",self.Public_var)
        print("Protected -> ",self._Protected_var)
        print("Private -> ",self.__Private_var)     # Private var can be acces by parent class

class child(parent):
    def child_access(self):
        print("The Child class access")
        print("Public -> ",self.Public_var)
        print("Protected -> ",self._Protected_var)

        try:
           print("Private -> ",self.__Private_var)   # private var cannot be access by sub class

        except AttributeError:
           print("Private Var cannot be access by sub classes")

class Stranger:
    def stranger_access(self, obj):
        print("The Stranger class access")
        print("Public -> ",obj.Public_var)
        print("Protected -> ",obj._Protected_var)

        try:
           print("Private -> ",obj.__Private_var)   # private var cannot be access but(if we use _parent__Private_var it will be use)

        except AttributeError:
           print("Private Var cannot be access by stranger classes")

p=parent()
print("\n Parent Class")
p.access_same()

c=child()
print("\n Child Class")
c.child_access()

s=Stranger()
print("\n Stranger Class")
s.stranger_access(p)     # To access parent class from stranger (We use the parent Object)


# Access method 

class bike:
    def one_public(self):                # public method
        print("Im public method")
    def _two_protected(self):            # Protected method
        print("Im Protected method")
    def __three_private(self):           # private method
        print("im private method")

    def access(self):                    # we can access a method from another method
        self.one_public()
        self._two_protected()
        self.__three_private()

class duke(bike):
    def d_access(self):
        self.one_public()
        self._two_protected()

        try:
            self.__three_private()        # cannot access a private method
        except:
            print("Cannot access the private method")

class car:
    def ca_access(self, obj):
        obj.one_public()
        obj._two_protected()

        try:
            obj.__three_private()         # cannot acccess a private method
        except:
            print("Cannot access the bike private method")



b=bike()
print("\n BIKESS")
b.access()

d=duke()
print("\n DUKE BIKE")
d.d_access()

c=car()
print("\n CARS")
c.ca_access(b)