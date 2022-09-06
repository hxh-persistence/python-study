#! usr/bin/python

a = 100

def test():
    global a
    print(sum(range(1, 101)))
    print(a)
    a = 101
    print(a + 1)

if __name__ == '__main__':
    test()
