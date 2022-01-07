#armstrong number 
number=input("Enter a number : ")
sum=0
for i in number :
    i=int(i)
    sum=sum+i**3
print(sum)
if int(number)==sum :
    print("a")
else:
    print("n")
    
