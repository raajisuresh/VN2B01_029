#key's value extract if present in both list and dict
list=['name','age','gender','state','role']
dict={'name':'hari','gender':'M','country':'IND','role':'Dev'}
#key=dict.keys()
#print(key,type(key))
print('_'*40)
for k in dict.keys() :
    for i in list :
        if k==i:
            print("value stored in '{}' key is '{}'".format(k,dict[k]))
print('_'*40)

