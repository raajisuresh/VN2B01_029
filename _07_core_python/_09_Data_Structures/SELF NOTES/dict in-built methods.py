#dict in-built methods
dict={}
dict.update({'s.no':1})
dict.update({'name':'raji'})
dict.update({'roll-no':'11x55A0417'})           #updating a dictionary
dict.update({'college':'SREC'})
dict.update({'university':'JNTUA'})
print(dict)

dict2=dict.copy()                               #copying a dict into dict2
print(dict2)
print(dict)
for i in dict:
    print('\t',i,'\t',dict.get(i))              #getting values by get method

print(dict.keys())                                    #getting keys

print(dict.fromkeys([1,2,3,4,5]))               #fromkeys method creates a dict by using a given argument
for i in dict.items() :                         #items method wil gives the key value tuple
    print(i,type(i))

print(dict.pop('roll-no'))                      #pops the  value of given key
print(dict)

print(dict.popitem())                           #pops the item i.e key and value
print(dict)

#print(dict.setdefault('gender','f'))
#print(dict)
dict.clear()
print(dict)