#Exception handling(Works for negative indecies also)
class Week:
    pass
    def day(self): 
            try:        
                list=['sun','mon','tues','wed','thurs','fri','sat']
                i=int(input("Enter a number : "))
                if True:
                    print(list[i-1])
            except Exception as e:
                print(e)
d=Week()
d.day()