# Exception handling

print("Welcome to the Zomato Food APP")
print("Please select Your Order")
try:                                                         # The code is crt means its try will be run
    number_of_items=int(input("Enter your order items"))
    total=number_of_items * 200
    print("Your Total Purchasing amount is : ", total)
    average_total=total/number_of_items
    print("Your average Purchasing amount is :", average_total)
except ZeroDivisionError:                                   # except to help from error
    print("Please choose a minimum one order to proceed")
    print("OR","\nGo to home page and select your item")

finally:                                                    # whatever happens its will run
    print("Thank you for using a Zomato")

print("Done")


