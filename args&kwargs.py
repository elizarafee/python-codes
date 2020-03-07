# Args and kwargs are two functional perameters. these are used to take multiple numbers in input as perameters.
# Args take input as a tuple (*args/*xxx)
# Kwargs returns input as a dictionary. this stands for key word arguments.

# *args & *kwargs:
def myFun(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I wiould like {} {}'.format(args, kwargs))
    print('I wiould like {} {}'.format(args[1], kwargs['food']))

myFun(10, 20, 30, 40, fruit = 'mango', food = 'Taru')