# Sets are unordered collections of unique elements...
# Can only be representative of the same object...
# Sets can't be sliced or indexed...
my_set = {1, 1, 1, 2, 1.3, 'books'}
print(my_set)                               # multiple 2'r wont be taken
print(len(my_set))                          # one object is taken only one time
my_set.add('prices')                        # adding objects
print(my_set)
my_list = [2, 3, 2, 3, 3]
print(set(my_list))
# print(my_set[1:])
# print(my_set[0])
