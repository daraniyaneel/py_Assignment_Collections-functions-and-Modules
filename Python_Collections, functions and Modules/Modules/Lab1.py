#Write a Python program to import the math module and use functions
#like sqrt(), ceil(), floor().

import math

num = float(input("Enter Any Number : "))

ans = math.sqrt(num)
print("The square root = ",ans)

num1 = math.ceil(num)
print("The ceiling value = ",num1)

num2 = math.floor(num)
print("The floor value = ",num2)
