#! usr/bin/python

# repeat remove
my_list = [1,1,3,3,4,5,6]
my_set = set(my_list)
print(my_list)
print(my_set)
my_list = [x for x in my_set]
print(my_list)