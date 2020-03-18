# Inheritence are the ability to re-use the code and reduce the complexity of a program
# It has One base class and one or multiple derive class

class Animal():
    def __init__(self, name):
        self.pername = name
    def bark(self):
        print('Animals barks differently!')

# Dog is inheriting Animal class
class Dog(Animal):
# In inheritence the methods also can be overrided 
    def bark(self):
        print("Dog barks like- 'Woof'")

# Dog is inheriting the Animal class so the methods of Animal class can be called by Dog class
dog = Dog('puppy')
print(dog.pername)

# The string has been changed by overriding
dog.bark()