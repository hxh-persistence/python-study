#! usr/bin/python

# sum(iterable[,start])
# iterable 可迭代的对象，列表，元组，集合 
# start 指定相加的参数，如果没有，默认为零

# range(start, stop[, step])
# start
# stop stopまで、でもstop含めない
# step

def testsum():
    # 10
    print(sum([1,2,3,4]))
    # 17
    print(sum([1,2,3,5], 6))
    # 5050 + 50
    print(sum(range(1, 101), 50))

if __name__ == '__main__':
    testsum()
