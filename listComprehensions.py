# List comprehensions are a unique way of quickly creating a list with python 
# useful for adding data in list for forloop and append()

myStr = 'hello world'
myList = []
for x in myStr:
    myList.append(x)
print(myList)

myList = []
#shortcut
myList = [x for x in myStr]
print(myList)

# If condition
myList = []
myList =[x for x in range(20) if x%2 == 0]
print(myList)


# else condition
myList = []
myList =[x for x in range(20)]
myList =[print(f'{x} is even') if x%2 == 0 else print(f'{x} is ODD') for x in range(20)]
print(myList)
