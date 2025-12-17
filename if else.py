# condition statement

age=20
if age > 18:
    print("you can vote")
else:
    print("you can't wait" )

mark=75

if mark >= 90:
    print("grade A")
elif mark>=70:
    print("grade B")
elif mark >=50:
    print("grade c")
else:
    ("study well")

# nested if

age =18
having_license="yes"
if age >=18:
    if having_license == "yes":
        print("you can drive")
    else:
        print("go and take license")
else:
    ("you are too young to drive")


# logical operation

score=80
attendance=70

if mark >=70 and attendance >=70:
    print("allow")
else:
    print("not allow")


recharge_amount=300
data_balance=1.5

if recharge_amount >= 350 or data_balance >= 1:
    print("you are eligible for the offer")
else:
    print("you are not eligible")

order_amount=2000
purchase_day="friday"
member_ship="yes"

# And Or logical operation

if (order_amount >=2000) and purchase_day in ("sunday","monday") or member_ship =="yes":
    print("you have discount")
else:
    print("you don't have discount")
