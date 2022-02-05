#Number guessing
from random import randint
class SmallValue(Exception):
    pass
class BigValue(Exception):
    pass
a=randint(0,9)
count=0
while count<3:
        try:
            ch=int(input("Enter a number : "))
            if a>ch:
                raise SmallValue
            elif a<ch:
                raise BigValue
            else:

                print("GREAT !!!!!!\nYOU HAD GUESSED A CORRECT NUMBER")
                break
        except ValueError:
            print("Invalid input")
        except BigValue: 
            print("Enter a small number")
        except SmallValue:
            print("Enter a big value")
        count+=1
else:
    print("YOUR CHANCES ARE OVER....\nBETTER LUCK NEXT TIME...")