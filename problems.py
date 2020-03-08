# write a program that returns the letter of two given numbers if both numbers are even, but return the greater if one and both numbers are odd
# problem 1:
def numbersss(a, b):
    if(a%2 == 0 and b%2 == 0):
        return (a, b)
    else:
        return max(a, b)

print(numbersss(4, 8))

# problem 2:
def words(a, b):
    if(a[0] == b[0]):
        return True
    else:
        pass

print(words('Tareque', 'Teliza'))
