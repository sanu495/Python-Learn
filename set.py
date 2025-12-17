# set is unordered
# set don't allow duplicate
# update without index delete the already value aand  new one 


a=[4,2,3,2]
b=set(a)
print(b)

movies1={"leo","rolex","kaithi","vikram","walter"}
movies2={"vikram","rolex","kappan","dark","dude"}

movies1.add("house of dragon")
print(movies1)

movies2.remove("vikram")
print(movies2)

movies1.discard("thug life") #check the set if not exists dont get error

print(movies1.union(movies2))
print(movies1.intersection(movies2))
print(movies1.difference(movies2))
print(movies2.difference(movies1))
