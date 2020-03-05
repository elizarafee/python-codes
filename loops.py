#Loops available in python : For/ While/ Do-while

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# For loop 
for num in a:
    print (num)

for num in a:
    if num % 2 == 0 and num != 0:
        print(f'even number {num}')
    elif num % 2 == 1:
        print(f'odd number {num}')
    else:
        print(f'undefined number {num}')

# While loop
b = 0
while b <= 10:
    if a[b] % 2 == 0 and a[b] != 0:
        print(f'even number {a[b]}')
    elif a[b] % 2 == 1:
        print(f'odd number {a[b]}')
    else:
        print(f'undefined number {a[b]}')
    b+=1

# # Do-While loop
# abcd = 1
# do
# {
#     print(f'Do-while loop number: {abcd}')
#     abcd = abcd + 1
# } while (abcd <= 5);

# for String
myString = 'Eliza Ahmed Rafee'
for num in myString:
    print(num)
#for Tuple
myTuple = (1, 2, 3)
for num in myTuple:
    print(num)

#for List
myList = [2, 4, 6, 8]
for num in myList:
    print(num)


myListOne = [(1,2), (3,4), (5,6), (7,8)]
for num in myListOne:
    print(num)
for a,b in myListOne:
    print(a, b)

#for Dictionary
myDict = {
    'k1' : 'value1',
    'k2' : 'value2',
    'k3' : 'value3',
    'k4' : 'value4'
}


# for keys retrieval (k1/ k2/ k3)
for num in myDict:
    print(num)

# for items retrieval(('k1', 'value1'), ('k2','value2'))
for num in myDict.items():
    print(num)

#for key-value retrieval(k1 value1, key2 value2)
for key,value in myDict.items():
    print(key, value)

#for key-value retrieval(value1/ value2)
for key,value in myDict.items():
    print(value)
