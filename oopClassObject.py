# OOP allows programmers to create their own objects that have method and attributes.
# OOP allow programmers to create code that is repeatable and organized
# Inside of a class a function is a object

class Printing():
    a = 120
    b = 340
    c = a + b
    def __init__(self, param1, param2):
        self.my_attribute1 = param1
        self.my_attribute2 = param2
 
printing = Printing(param1 = 'eliza', param2 = 24)
print(printing.my_attribute1)
print(printing.my_attribute2)