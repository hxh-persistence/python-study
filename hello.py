#! usr/bin/python

a = 100

def test():
   b = 2
   for b in range(3,10,2):
    print(b)

def sayhello():
    print('hello')
    for i in range(0, 19):
        print(i)

if __name__ == '__main__':
    test()
    sayhello()
