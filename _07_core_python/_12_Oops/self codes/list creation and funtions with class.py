a=10
class Exercise:
    def __init__(self,a):
        self.a=a
    def obj(self):
        a=int(input("how many elements you want in an object ..."))
        self.a=[]
        for i in range(0,a):
            element=input("Enter an element : ")
            self.a.append(element)
        print('Given list : ',self.a)
    def elements(self):
        print("Elements---")
        for i in self.a:
            print(i)
    def indices(self):
        print("Indices---")
        for i in self.a:
            print(self.a.index(i))
    def sum(self):
        print("Length of object---\n",len(self.a))
        sum=0
        for i in self.a:
            sum=sum+int(i)
        sum=sum+a                               #a is global variable
        print("Sum of elements---\n",sum)
l=Exercise(1)
l.obj()
print(type(l.obj),type(l.sum),type(Exercise))
l.elements()
l.indices()
print(type(l))
print(l.sum())