# string function 

mobile="9150348279"
masked=mobile[:2]+"******"+mobile[-2:]  # filter the what number we want to show
print(masked)

song="minNAle MInNaLe"
artist="hArris jaYARAj"
print(f"{song.title()} - {artist.title()}") # print the value a correct capital format

drop="chennai"
change_location=drop.replace("chennai","thiruvanthapuram").title()
print(change_location)  # replacing a existing value

message="your booking id is : UUIS789. please don't share to anyone"
booking=message.split(":")[1].split(".")[0].split()
print(booking)   # spliting a string value for separate reading


zomato="the code is available in FGS089"
if "FGS089" in zomato:
    print("code is available")

feedback="the driver was so polite and the ride was smooth"
print("position is :", feedback.find("smooth"))  # find the letter index

name="sanoop sanu"
intial="".join([word[0].upper() for word in name.split()])
print(intial) # word refers a word inital letter

value_in="   Thunder bolt   "
print(value_in)
clean=value_in.strip()  # strip is use for remove the space
print(clean)

word="the trip was amazing and the car was clean"
print(len(word))    # count the all including spaces

word_count=len(word.split())
print(word_count)  # count the word not space

