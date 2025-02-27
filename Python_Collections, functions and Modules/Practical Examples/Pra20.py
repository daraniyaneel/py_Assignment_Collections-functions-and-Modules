#Write a Python program to create a parameterized function that takes
#two arguments and prints their sum.

def add(a,b):
    return a+b

a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

sum =add(a,b)

print("Sum = ",sum)
