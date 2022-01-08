'''for x in "YASHWIK SRINIVAS" :
    print(x,end=",")

str="RAJESWARI"
i=0
while i<len(str):
    print(str[i],end=",")
    i+=1'''
'''#string indexing
str="YASHWIK"
#forward indexing
print(str[2])
print(str[4])
#negative indexing
print(str[-2])
print(str[-5])
#forward slicing'''
'''str1="YASHWIK"
print(str1[0:7])
print(str1[:])
print(str1[0:])
print(str1[:7])
print(str1[::2])
print(str1[::-1])'''
#negative slicing
'''str2='suresh'
print(str2[-5:-1])
print(str2[-6:])
print(str2[::-1])
print(str2[-5::2])'''

'''#string slicing
text="YASHWIK SRINIVAS"

print(text)'''

#string Methods/functions
text1='Hai!!! How Ar\te You...???         '
print("capitalize : ",text1.capitalize())
print('casefold : ',text1.casefold())
print('center : ',text1.center(30,'.'))
print("count of 'a' : ",text1.count('a'))
print("encode : ",text1.encode())
print("endswith : ",text1.endswith('a'))
print("expandtabs : ",text1.expandtabs(10))
print("find 'y' : ",text1.find('y'))
text2='{hai}!!! How are you...???'
print(text1)
print("format : ",text2.format(hai='Hi'))
#print("format_map() : ",text2.format_map(map:{'Hello'}))
print("index : ",text1.index('u'))
print("isalnum : ",text1.isalnum())
print("Isalpha : ",text1.isalpha())
print("Isdecimal : ",text1.isdecimal())
print("Isdigit : ",text1.isdigit())
ha="_23"
print("Is identifier : ",ha.isidentifier())
print("islower : ",text1.islower())
print("isnumeric : ",text1.isnumeric())
print("isprintable : ",text1.isprintable())
print("is space : ",text1.isspace())
print("is title : ",text1.istitle())
print("is super : ",text1.isupper())
print("join : ","Hello".join(text1))
print("l just : ",text1.ljust(50))
print("lower : ",text1.lower())
print("l strip : ",text1.lstrip())
text3=text1.maketrans('How','Who')
print("make transition : ",text1.translate(text3))
print('partition : ',text1.partition('H'))
print('replace : ',text1.replace('How','Where'))
print('r find : ',text1.rfind('>'))
print('r index : ',text1.rindex("!"))
print('r just : ',text1.rjust(70))
print("r partition : ",text1.rpartition('H'))
print("split : ",text1.split())
print("Uppercase : ",text1.upper())
print("ower : ",text1.lower())
print(text1.splitlines())
print(text1.zfill(40))
print(text1.swapcase())
print(text1.title())