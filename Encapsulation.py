# Encapsulation

class order:
    def __init__(self, customer_name, items, total, discount):
        self.customer_name=customer_name
        self.items=items
        self.__total=total           # Private variable
        self.__discount=discount     # Private variable

    def __calculation(self):             # Private Method
        return self.__total - self.__discount

    def _admin_view(self):                      # Protected Method
        return {
            "Customer_Name" : self.customer_name,
            "Items" : self.items,
            "Total" : self.__total,   
            "Discount" : self.__discount,
            "Final amount" : self.__calculation()        # Privated method called by another method
        }
    def _Customer_view(self):                  # Protected Method
        return {
            "Customer_Name" : self.customer_name,
            "Items" : self.items,
            "Final amount" : self.__calculation()}   # private Method 

class Admin:
    def admin_access(self, Order):     # Order is object of class order
        return Order._admin_view()     # Parent class method
class customer:
    def customer_access(self, Order):  # Order is object of class order
        return Order._Customer_view()  # Parent class method


Order=order("sanoop", ["mango","orange","apples"], 590, 79)

admin=Admin()
print("ADMIN VIEW")
print(admin.admin_access(Order))

cus=customer()
print("CUSTOMER VIEW")
print(cus.customer_access(Order))