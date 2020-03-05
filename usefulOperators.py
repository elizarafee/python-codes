# range() / checking(IN, Max, min) / enumerate() / zip() 
# enumerate() represents the value with index of any lists, tuples and so on
# Zip() connects elements from different lists or tuples with considering it's index value

# range().. printing 0-9
for num in range(10):
    print(num)

# printing 3-9
for num in range(3,10):
    print(num)

# printing 0-10 with step 2
for num in range(0, 11, 2):
    print(num)

# Checking by IN
print('x' in 'love')
print('T' in 'Tareque')

index = 0
for num in 'You still exists in my 100% Mr.Tareque':
    print(f'at {index} the value is {num}')
    index+=1

# getting values with it's index
myList = ['a', 'b', 'c', 'd']
for num in enumerate(myList):
    print(num)

for index, value in enumerate(myList):
    print(index, value)
    print('\n')

# Zip()
myList1 = ['a', 'b', 'c', 'd', 'e']
myList2 = [1, 2, 3, 4, 5]
myList3 = [1.20, 3.21, 3.43, 4.21, 5.32]

a = zip(myList1, myList2, myList3)

for num in a:
    print(num)

b = list(zip(myList1, myList2, myList3))
print(b)

c = tuple(zip(myList1, myList2, myList3))
print(c)

# Checking from list
print('ab' in ['abcde', 'ab', 'cds'])

# Checking from tuple
print('ab' in ('abcde', 'ab', 'cds'))

# Checking dictionary by key
print('ab' in {'a' : 'abcde', 'c' : 'cds', 'ab' : 'love'})

# Checking dictionary by value
print('ab' in {'a' : 'abcde', 'c' : 'cds', 'ab' : 'love'}.values())

print(max(myList3))
print(min(myList3))