#! usr/bin/python
def test1():
    x = 1
    y = 1
    print(x, end = " ")
    print(y, end = " ")
    while(True):
        z = x + y
        x = y
        y = z
        if (z > 100):
            break
        print(z, end = " ")

if __name__ == '__main__':
    test1()