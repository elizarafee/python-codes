# how to pass a function as an argument

def funcname():
    return 'Hi Jose!'

def other(a):
    print('other function runs here')
    print(a())

other(funcname)