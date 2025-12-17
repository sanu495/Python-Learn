# Function Composition

def add(x):
    return x + 2
def multi(x):
    return x * 2
def Composition(x):
    return add(multi(x)) # composition

print(Composition(5))

# Callback Function

def but_click(Callback):
    print("Button clicked")
    Callback()

def show_details():
    print(" hi sanoop welcome")

but_click(show_details)


# Recursive Function

# A recursive function thats calls itself
# in order to solve a smaller version of the same problem

def factorial(n):
    if n==1:
        return 1
    return n * factorial(n - 1)    # This function calling itself repeated still condition became to true

print(factorial(5)) 

def countdown(n):
    if n==0:
        print("BOOM")
        return
    print(n)
    countdown(n-1)

print(countdown(5))


# Generator Function with Yield

# Generator Function is special type of function that uses the yield keyword
# to return values one by one , instead of returning everything at once

def get_num(n):
    for i in range(n):
        yield i

for num in get_num(5):
    print(num)


    