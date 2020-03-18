# In the case of abstract there have to be at least two classes one is the base class and the others are called derive class where the 'raise' keyword used methods from the base class have to be implemented on the derive class
class animal ():
    def __init__(self, name):
        self.name = name
    # this method have to be implemented on the subclasses --> 'raise'
    def speak(self):
        raise NotImplementedError("Subclass must implement the method")

class Dog(animal):
    def printing(self):
        print("Hello method")
    
    def speak(self):
        print('without implemented this method in the derive class this will show an error')

dog = Dog('Puppy')
dog.speak()