#variable length arguments
class Addition:
    def add(self,*a):
        print(a)

        for i in a:
            print(i)

add1=Addition()
add1.add(1,2,34)