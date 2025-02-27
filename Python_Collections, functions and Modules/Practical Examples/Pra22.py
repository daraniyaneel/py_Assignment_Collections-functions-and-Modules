# Write a Python program to create a lambda function with two expressions.

a = int(input("Enter first number : "))
b = int(input("Enter second number :"))

max = lambda x,y: x if x>y else y

print("Maximam = ",max(a,b))
