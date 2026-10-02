#Program 1: Built-in Module (math)
import math 
num = 16 
print("Square root:", math.sqrt(num)) 
print("Factorial:", math.factorial(5))
print("Power:", math.pow(2, 3))
print("Log:", math.log(10))

# program 2
from functools import reduce 
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers) 
print("Sum using reduce:", result)

# program 3
#Step 1: Create file my_module.py
def add(a, b): 
    return a + b 
def multiply(a, b): 
    return a * b


