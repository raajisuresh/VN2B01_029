#tuple from user input
tuple_ele=int(input("Enter how many elements do you want ...???..."))
list=[]
for i in range(tuple_ele):
    j=input("Enter element of tuple : ")
    list.append(j)
tuple=tuple(list)
print("Given Tuple : ",tuple)