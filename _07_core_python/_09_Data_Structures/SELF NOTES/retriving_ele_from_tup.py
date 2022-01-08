#Retriving elements from tuple
tuple=('yash','harsh','surya','hari',[1,2,3,4],('a','b','c','d'))
for i in tuple :
    print("\n{} indexed element of tuple is {}".format(tuple.index(i),i),'-'*10)
    for j in i :
        print("{} indexed element of tuple{} is {}".format(i.index(j),[i.index(j)],j))
    
    print("_"*50)