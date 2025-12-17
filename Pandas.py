# Pandas is a Powerful python library used for data analysis and manipulation

# Data Frame is the core data structure in pandas(excel sheet, sql table)

import pandas as pa

data={
    "Name": ["Alice","Bob","Sanoop"],
    "Age": ["25","20","22"],
    "City": ["Madurai","OOty","Kanniya kumari"]
}

df=pa.DataFrame(data)   # DataFrame is used for range the data into rows and columns
print(df)
print(df.dtypes)       # Show the Datatypes of the data
print(df["Name"])      # Show Name key values only

pf=pa.read_csv("data.csv")    # It read the data.csv file and give the output
pf["Age"].to_csv("output.csv", index=False)  # Its send data to another file 

pp=pa.read_csv("product.csv")

# Step 2: Add new column -Total

pp["Total"] = pp["Price"] * pp["Quantity"]

# Step 3: group by Product

grouped=pp.groupby("Product")["Total"].sum().reset_index()

# Step 4: Sort by Total Sales
sorted_pp=grouped.sort_values(by="Total", ascending=False)

print("sales summary")
print(sorted_pp)

# Join Table

# Customer Table

customers=pa.DataFrame({
    "CustomerID" : [1,2,3],
    "Name" : ["Alice","Sanoop","Sanu"]
})

# Orders Table

orders=pa.DataFrame({
    "OrderId" : [1, 2, 3],
    "CustomerID" : [1, 2, 3, 1],
    "Product" : ["Shirt", "pant", "Shoe", "hat"]
})

result=pa.merge(customers,orders, on="CustomerID", how="inner")
print("Inner Join")
print(result)


# Specify pass header Name in column 

df=pa.read_csv("data.csv", header=None, names=["Name","Age","City"])

print(df)








