#Write a Python program to create a calculator using functions.

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

print("1. ADD")
print("2. SUB")
print("3. MUL")
print("4. DIV")

ch = int(input("Enter Your Choice : "))

if ch==1:
    a = add(a,b)
    print("ADD = ",a)
elif ch==2:
    s = sub(a,b)
    print("Sub = ",b)
elif ch==3:
    m = mul(a,b)
    print("Mul = ",m)
elif ch==4:
    d = div(a,b)
    print("Div = ",d)
else:
    print("Enter Valid Choice ")
