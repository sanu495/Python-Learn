# Function

def great():
    print("welcome to the function")
great()

#parameter passing function

def know(name):
    print(f"hello {name}, Welcome")
know("sanoop")

def add(a,b):
    print(a+b)
add(4,6)

# Return Function 

def total(a,b,c):
    return a+b+c
result=total(34,56,78)
print(result)

# args function

def cal(*args):
    total=0
    for num in args:
        total+=num
        #0+=1
        #1+=2
        #3+=2
        #5
    return total
print(cal(1,2,2))
    
# kwargs function

def profile(**kwargs):
    print("Your Profile")
    for key, value in kwargs.items():
        print(f"{key} -> {value}")
profile(name="Sanoop",age=22,Email="sanoops58@gmail.com",place="france")











