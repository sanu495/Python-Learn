# Lambda Function

add=lambda a,b: a+b  # Single Line Lambda Function
print(add(4,6))

Square=lambda x: x*x
print(Square(5))

# Map with Lambda

fruits=["mango","orange","apple"]
result=list(map(lambda fruit:fruit.upper(),fruits))       # Map apply condition to every index value
print(result)

# Filter With Lambda

nums=[1,2,3,4,5,6,7,8]
even=list(filter(lambda x : x%2==0, nums))             # Filter gives output only condition matches value
print(even)


# Reduce with Lambda

from functools import reduce

no=[2,3,4,6,7]
total=reduce(lambda a,b: a + b,no)
print(total)

num=[23,45,66,8]
greater=reduce(lambda a,b: a if a>b else b, num)       # Reduce take many value and give one output 
print(greater)


# Example

prices=[340,56,7890,4577,90]
opera=list(filter(lambda x: x>2000,prices))
aver=reduce(lambda a,b: a+b,opera)
print(aver)

