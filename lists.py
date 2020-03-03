# LISTS are ordered sequences that can hold a variety of object type
# ex: a = [1, 1.3, 'Tareque']
# supports Indexing and slicing
# Lists can be nested and have useful methods

my_list = [1, 1.3 , 'Hasan', 'Mohammad', 'Tareque']
print(len(my_list))
print(my_list[1])
print(my_list[2:])
my_2nd_list = ['Eliza', 'Ahmed', 'Rafee']
new_list = my_list + my_2nd_list                       # concatanation
print(new_list)

my_2nd_list[1] = 'Tareque'                             # changing value of set
print(my_2nd_list)

my_2nd_list.append('Hasan')                            #  adding value in list
print(my_2nd_list)

my_list.pop(0)                                         # deleting value from list
print(my_list)
my_list.pop(0)
print(my_list)

number_list = [3,2,4,2,5,1,7,4,7]
print(number_list)
number_list.sort()                                     # sorting
print(number_list)


number_2nd_list = [3,2,4,2,5,1,7,4,7]
print(number_list)
number_2nd_list.sort()
a = number_list
print(a)

c = number_2nd_list.sort()                             # can't reassigned in this way so the type of C will be None
print(c)

number_3nd_list = [3,2,4,2,5,1,7,4,7]                  # reversing list
number_3nd_list.reverse()
print(number_3nd_list)