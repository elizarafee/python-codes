# taking input from user
# input function takes data as a string

result = input('Enter a number: ')
print(result)

print(type(result))

# changing type doesn't change it parmanently
print(float(result))
print(type(result))

# have to declare the data type if necessary it also cant be changed parmanently
res = int(input('Enter a number: '))
print(type(res))
print(float(res))
print(type(res))