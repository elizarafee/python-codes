# Some of the loop controlling keywords are: break/ continue/ pass

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in a:
    if num==4:
        continue
    elif num==8:
        break
    else:
        print(num)

b = []

# error will be shown coz nothing is done in the loop. For getting rid of this problem there's a key to use 'pass'
# => for num in b:
for num in b:
    pass