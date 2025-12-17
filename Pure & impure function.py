#Pure and Impure Function


# Impure Function
Total=0

def add(amount):
    global Total     # This Function changing a outside variable or method called(Impure function)
    Total+=amount
    print(Total)    # -> Output 4

add(4)

def sun():
    print(Total)    # -> Output 4 but How 

sun()

value=0

# Pure Function

def sub(user):
    value=0
    value+=user       # This function cannot change the outside variable or method(Pure Function)
    print(value)      # -> Output 8

sub(8)

def mul():
    print(value)      # -> Output 0

mul()