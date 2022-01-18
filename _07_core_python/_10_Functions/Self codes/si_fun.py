#program to calculate SI by using function
#without parameters and with return type
def si():
    p=float(input("The principle amount : "))
    t=float(input("The time for intrest in years : "))
    r=float(input("The rate of intrest in percentage : "))
    si=(p*t*r)/100
    return si
print(si())

#Without parameters and without return type
def si1():
    p=float(input("The principle amount : "))
    t=float(input("The time for intrest in years : "))
    r=float(input("The rate of intrest in percentage : "))
    si=(p*t*r)/100
    print(si)
si1()

#with parameters and with return type
def si2(p,t,r):
    si=(p*t*r)/100
    return si

p=float(input("The principle amount : "))
t=float(input("The time for intrest in years : "))
r=float(input("The rate of intrest in percentage : "))
print("Intrest amount is ",si2(p,t,r))

#with parameters and without return type
def si3(p,t,r):
    si=(p*t*r)/100
    print(si)

p=float(input("The principle amount : "))
t=float(input("The time for intrest in years : "))
r=float(input("The rate of intrest in percentage : "))
si3(p,t,r)