#Retriving iterable(STRING) object elements by function
#function defination
def elements(a,b):
    print(" Elements of the given text : ","\n","_"*25)
    for i in range(0,len(a)):
        print("Element at {} index is '{}'".format(i,a[i]))
    print("\nLength of the given text : ",len(a))
    print("Entered text : ",a)
    print("Concatenation of given text : ",a+b)
    print("_"*40)
    
#Function calling
a=input("Enter any thing : ")
b=input("Enter another text : ")
elements(a,b)