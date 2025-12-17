a=20
b=5

#arithematic operation
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b) #20*20*20
print(a//b) #not print a . after value


#Comparsion operation

x=30
y=8

print(x==y)
print(x!=y)
print(x<y)
print(x>y)

#logical operation

e=True
i=False

print(e and i)
print(e or i)
print(not e)
print(not i)



#Examples

amount=10000
tax=amount * 0.28
total=amount + tax
print(total)
if total > 10000:
    discount=total * 0.10
    total-=discount
    print(f" your total amount is {total} with disount")

else:
    print("you are not eligible for discount")

age=50
student="yes"

if age<18 and student=="yes":
    print("yes discount")
else:
    print("no disount")
