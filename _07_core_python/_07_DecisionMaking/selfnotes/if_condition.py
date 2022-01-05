#By using comparing and logical operators
'''marks=int(input("Enter the marks : "))
if marks>=0 and marks<=100 :
    print( "Marks : ",marks)
if marks>=0 and marks<35 :
    print("candidate cannot get the required marks")
if marks>=35 and marks<=60 :
    print("Candidate is passed in FIRST class")
if marks>60 and marks<=75 :
    print("Candidate passed with distinction")'''

#By using membership operators
'''List=['y','a','s','h','w','i','k']
ch=input("Enter a character : ")
if ch in List :
    print('A valid character')
if ch not in List :
    print("It is not a valid character")'''



#By using identity operators
'''Tuple=tuple(input("Enter any value : "))
Tuple1 =tuple(input("Enter any value : "))
Tuple2 =(23,25)
Tuple3 =(23,25)
Tuple4 =(23)
t=[24]
#print(type(Tuple2),type(Tuple3),type(Tuple4),type(t))
if Tuple2 is Tuple:
    print('Tuple2 and Tuple are in same location')
if Tuple1 is Tuple2 :
    print("Tuple1 and Tuple2 are in different location")
if Tuple is not Tuple1 :
    print('Tuple and Tuple1 are in different location')
#print(id(Tuple),id(Tuple1),id(Tuple2),id(Tuple3))'''

'''x=25
y=int(input("enter a number"))
print(id(x),id(y))'''



#By using arithmetic,assignment and comparative operators
'''x=25
y=100
number=int(input("enter a number from 1 to 10 : "))
if(x*number==y/4):
    print("x is one fourth of y")
if(x*number==y/2):
    print("y is four times of x")
if(number*x == y) :
    print("y is product of x and number")
if(number == x/number) :
    print("x is a square of number")
if(number**2==y):
    print("Square root of y is number")'''