def add(a,b):
    return a+b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b == 0:
        return " error: Divide by zero not alowed"
    return a / b 
while  True :
    print("\n simple calculator")
    print("1. ADD")
    print("2.SUBTRACT")
    print("3.MULTIPLY")
    print("4.DIVIDE")
    print("5. EXIT")
    choice = input("enter yor choice")
    if choice == "5":
        print("calculator off")
        break
    a = float(input("enter first number"))
    b = float(input("enter second number"))
    if choice == "1":
        print("Result",add(a,b))
    if choice == "2":
        print("Result",subtract(a,b))
    if choice == "3":
        print("Result",multiply(a,b))
    if choice == "4":
        print("Result",divide(a,b))
    else:
        print("invalid choice")
   

