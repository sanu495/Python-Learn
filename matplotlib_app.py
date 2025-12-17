import matplotlib.pyplot as plt
import csv

# Plot show

x=[3,5,6,4,8]
y=[10,20,28,30]

plt.plot(x,y)
plt.title("simple line plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()

# Bar Show

x=["Apple","Banana","Grapes"]
y=[10,15,45]

plt.bar(x,y, color="green")
plt.title("Fruit Count")
plt.ylabel("count")
plt.show()

# Scatter Show

x=[1,2,3,4,5]
y=[5,20,15,25,10]

plt.scatter(x,y, color="red")
plt.title("simple scatter plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()


# Reading csv files and show plot view

# Intialize empty lists

months=[]
sales=[]

# Read csv files

with open("data.csv","r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        months.append(row["months"])
        sales.append(int(row["sales"]))

# Plot the data
        
plt.plot(months,sales,marker="0")
plt.title("Monthly sales report")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.show()
