cars=["BMW","mclaren","Bugatti","ferrai","dodge"]

#list method

cars.append("mustang")
print(cars)

cars.remove("BMW")
print(cars)

print(cars.count("Mustang"))

cars.insert(3, "ford")
print(cars)

cars.reverse()
print(cars)
 
cars.pop()
print(cars)

print(cars[0:2])

print(cars[2:5])

print(cars[-3])


if "BMW" in cars:
    print("yes")

else:
    print("NO") 



for i, location in enumerate(cars):
    print(f"{i} {location}")




