# Tuples are very similar to lists  but there are immutable
# lists a = [1, 2, 3] || tuples a = (1, 2, 3)

my_tuple = (1, 'Tareque', 1.3)
print(my_tuple[1:])

my_2nd_tuple = (2, 'Tareque', 2, 1, 1, 2)
print(my_2nd_tuple.count(2))
print(my_2nd_tuple.index('Tareque'))
#my_2nd_tuple[0] = 1                             # value is not changable