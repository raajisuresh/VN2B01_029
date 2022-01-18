#list creation
list=[]

#1.Appending elements             
list.append(1)
list.append(2)
list.append([1,2,3])
print(list)                                  #adds the single element at last position
list.append(('r','a','j','i'))
list.append('a')
print(list)                        
print("_"*30)
#2.list copying
list1=list.copy()                              #copying the complete to list to second list
print(list1)
print("_"*30)
#3.count method
print(list.count('a')) 
print("_"*30)
                                                #counts the given element frequency

#4.extending a list
list.extend([1,2,3,'raji'])                    #It can adds multiple elements at last position 
print(list)
print("_"*30)


#5.finding index of an element
print(list.index('a')) 
print("_"*30)
                                            #It will gives index of the given element

#6.inserting into a list
list.insert(4,'yash')                          #inserts the given element at a given index 
print(list)
print("_"*30)
#7.element poping
list.pop()                                      #removes the last indexed element of a list
print(list)
print("_"*30)
#8.remove method
list.remove(list[5])                            #removes the given indexed element
print(list)
print("_"*30)
#9.list reversing
list.reverse()                                 #reverse the list elements
print(list)
print("_"*30)
#10.list ascending and descending order
list3=['ab','de','qr','q','cf','c']
list2=['a','d','r','q','f','c']
list2.sort()                                #sorts in ascending order
print("sort",list2)
list3.sort(reverse=True)                    #sorts in descending order
print(list3)
print("_"*30)
#11.clearing a list
list2.clear()                               #clears the elements of list
print(list2)