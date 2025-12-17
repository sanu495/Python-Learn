from abc import ABC, abstractmethod

# Abstraction
 
class manager(ABC):

    @abstractmethod
    def login(self):
        pass

    @abstractmethod
    def logout(self):
        pass

    @abstractmethod
    def check_out(self):
        pass

class employee(manager):           # In abstraction if we mention abstract in parent function top 
                                   # confirm we have to use that in child function
    def login(self):
        print("yes im login")
    def logout(self):
        print("yes im logout")
    def check_out(self):
        print("im checking in sir")

emp=employee()
emp.check_out()
emp.login()
emp.logout()

    