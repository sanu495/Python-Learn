# File Handling

file=open("note.txt","w")                # file overWrite or create(now creating)
file.write("welcome to the file handling\n")
file.write("You are awesome\n")
file.close()

file=open("note.txt","r")               # file reading
content=file.read()
print("file content\n",content)
file.close()

file=open("note.txt","a")               # file appending (adding a new content with existing file)
file.write("Adding a new line\n")
file.close()

with open("note.txt","r") as file:      # with is helping for we dont need to close a file its automatically done
    for line in file:          
        print(line.strip())             # strip use for remove space


# input from user example
        
feeback=input("Enter Your Feedback : ")
 
with open("Feeback_one.txt","a") as file:
    file.write(feeback + "\n")
    print("Thanks for your feedback")

with open("Feeback_one.txt","r") as file:
    print(file.readline().strip())        # Read a single line

with open("data.txt") as f:
    while True:
        line=f.readline()                    # Its run still found "error"
        if not line:                         # if we using while loop use can use readline
            break
        if "error" in line:
            print("Found Error :", line.strip())

with open("data.txt") as line:              # if we want limit value use readline or read
    for _ in range(4):                      # In for loop we canno't assign the variable instead we use in print
        print(line.readline().strip())

with open("database.csv","r") as dataread, open ("output.csv","w") as outline:
    for f in dataread:
        print(f.strip())                 # In this case we frst open a file and read and write that content to new file
        outline.write(f)                # outline is new file to write from read file


# CSV File means comma separate value
    
import csv

with open("database.csv", "r") as fine:
    reader = csv.DictReader(fine)          # Dictreader read file by csv model header,column , row
    for row in reader:
        print(row['id'])                   # we assign a id header to find id value


with open("database.csv", "r") as file:
    lines=file.readlines()
    for line in lines[1:]: # skip header
        columns=line.strip().split(",")   # split helps to arrange data by index value
        print(columns[2])
