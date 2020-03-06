# Functions allows us to create blocks of code that can be easily executed many time without needing of writing
# the same code repeatedly
# function writing stars with 'def' and the function name  should be all  lower case letters
# 'return' allows us to assign the output of the funtion to a new variable
# For future better understanding about the method or code programmer should use docstring
# for knowing about the function name_function(after taking the cursor here press(shift+tab))/ help(name_function)
def printing_func():
    print('Printed by a function')

def sum_of_numbers(a = 90, b = 10):      # the value of a and b are taken in default for ignoring the error if the value is not given
    '''
        docstring : information about the function
        input : two value
        output : summation of the values
    '''
    return a+b



printing_func()
print(sum_of_numbers(20))