#dict from user input
dict1={}
n=int(input("Enter how many key, vaue pair you want...."))
for i in range(n):
    key=(input("Enter a key : "))
    val=input("Enter a value for key :")
    dict1.update({key:val})
print(dict1)