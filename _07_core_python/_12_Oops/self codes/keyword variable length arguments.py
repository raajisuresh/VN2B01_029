#keyword variable length arguments
class Addition:
    def add(self,**a):
        print(a)

        for i in a.values():
            print(i,end=' ')

add_=Addition()
add_.add(a='Hiiii!!!',b='Hellooooo',b1='How r u ..?')
add_.add(a='Keyword variable length arguments',b='save in dict type')