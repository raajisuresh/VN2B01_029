#Exception handling
try:
    num1=int(input("Enter a number : "))
    num2=int(input("Enter a second number : "))
except ValueError:
    print("Invalid input")

