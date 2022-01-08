#Tuple in built methods

#tuple creation
print('_'*50,'\n')
print("Tuple creation-----")
tuple=()
print("\ntuple : ",tuple,type(tuple))        #Empty tuple creation
tuple1=("bhima")                
print("\ntuple1 : ",tuple1,type(tuple1))      #though it is in paranthesis it is a string
tuple2=("bhima",)
print("\ntuple2 : ", tuple2,type(tuple2))      #By using comma it became as a tuple
tuple3=('abhi','balu',100,['A','B','C'],{'name':'pranya'})
print('\ntuple3 : {}'.format(tuple3))
tuple4=(1,2,3,4,5)
print('\ntuple4 : ',tuple4)
tuple5=('x','r','raji','yash')
print('\ntuple5 : ',tuple5)
print('_'*50,'\n')

#in_built methods of tuple
#tuple.append(10)                           #We can't add elements into a tuple ,becuse tuple is an immutable object
print("In-built methods of tuple-----")
print('\n1)count of "balu" in tuple3 : ',tuple3.count('balu'))      #count method wil gives the frequency of the given element
print('\n2)Index of 100 in tuple3 : ',tuple3.index(100))
print("\n3)Length of tuple3 : ",len(tuple3))        #length function gives no.of elements of a tuple
print("\n4)maximum element of tuple4 : ",max(tuple4))
print("4)maximum element of tuple5 : ",max(tuple5))   #gives the higher order element based on ascii table
print('\n5)minimum of tuple4 : ',min(tuple4))
print('5)minimum of tuple5 : ',min(tuple5))             #gives the lower order element based on ascii table
print('_'*50,'\n')

#Indexing in tuple
print('Idexing in tuple------')
print('\nThird index element of tuple3 : ',tuple3[2])
print('\nLast element of tuple3 with negative indexing : ',tuple3[-1])
print('_'*50,'\n')

#Slicing in tuples
print('Slicing in tuples-----')
print("\nSome elements of tuple4 by using slicing : ",tuple4[1:5])
print('_'*50,'\n')




