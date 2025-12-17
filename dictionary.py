# key value pair
# don't allow duplicate

Student={
    "stu_id":"std978",
    "name":"sanoop",
    "age":"22",
    "email":"sanoops58@gmail.com",
    "class":["school","highschool","college"],
    "stu_id":"2023578" #don't allow duplicates instead of overwrite the existed id
}

print(Student["age"]) #lookup with key
print(Student.get("college")) # lookup with value get none instead of error

print(Student.keys())
print(Student.values())

for key, value in Student.items():
    print(key,":",value)


Student.update({"dob": "20-10-2002"})
print(Student)

Student.update({"dob":"20-10-2003"})
print(Student)

Student.pop("class")
print(Student)

print(Student["class"][2]) #find the value by index

for study in Student["class"]:
    print(study)


trips= {
    "UUISF7":{"trip_id":"UUISF7","pickup":"Chennai","drop":"airport","fare":589},
    "UUISi6":{"trip_id":"UUISi6","pickup":"Thiruvanthapuram","drop":"central","fare":890},
    "UUIS57":{"trip_id":"UUIS578","pickup":"ooty","drop":"hillstation","fare":345}
}

print(trips["UUISF7"]["pickup"])

for Trip_id, details in trips.items():
    print(Trip_id)# print key value
    print(details["pickup"],"->",details["drop"])

