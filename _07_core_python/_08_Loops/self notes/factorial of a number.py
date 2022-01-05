#factorial of a number
number=int(input("Entera number : "))
factorial=1
for i in range(1,number+1) :
    factorial=factorial*i
print(factorial)