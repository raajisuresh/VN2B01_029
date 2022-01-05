#divisable by 11 but not by 2 from 100 to 500
'''for i in range(100,500) :
    if i%11==0 :
        if i%2!=0 :
            print(i,end=",")
    else :
        pass'''


for i in range(100,500) :
    if i%11==0 :
        if i%2==0:
            continue
        else:
            print(i,end=",")