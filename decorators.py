# EXAMPLE 1
def func():
    return 1

print(func())
new_func = func
print(new_func())

del func
#print(func())
# func function has been deleted but the new_func still exists
print(new_func())

# EXAMPLE 2
def fun1(A = 'Tareque'):
    print("this is the main function")

    def fun2():
        return "\tthis is the nested function for 'Tareque'"
    
    def fun3():
        return '\tthis is the function for others'

    if A == 'Tareque':
        print(fun2())
    else:
        print(fun3())

hello = fun1
hello()
fun1('Tareque')
hello('Hasan')