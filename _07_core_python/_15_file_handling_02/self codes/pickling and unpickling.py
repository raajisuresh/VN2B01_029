#pickling and unpickling
import pickle
try:
    file1=open('pickle.dat','wb')
    pickle.dump('test.txt',file1)
    c=open('pickle.dat','rb')
    a=pickle.load(c)
except EOFError:
    print('File came to end...')