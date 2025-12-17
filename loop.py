# loops in python

names=["sanu","sebi","sanoop","sebina"]
for test in names:
   print(test.upper())    # for loop

correct_pin="2335"
entered_pin=""
while correct_pin != entered_pin:
    entered_pin=input("enter you correct pin") # while loop
print("Access granted")
Break

boys=[1,2,3,7,9,8,6,4,0,5]
for x in boys:
    if x==5:
        print(" mr 5 I find you")
        break
    print(x)

# continue

n=(20,40,-6,-7,-70,56,89)
for i in n:
    if n < 0:       # remove less than 0 num and print
        continue
    print(i)

# pass

n=(20,40,-6,-7,-70,56,89)
for i in n:
    pass # future logic for print


count=5
while count > 0:
    print(f"countdown is {count}")
    count-=1

print("Times up")

# infinite loop and logic inside loop

items=[]
while True:
    item=input("Add the items in  your cart('you finish your shopping enter done'): ")
    if item.lower() == "done":
        break
    items.append(item)
print(items)












