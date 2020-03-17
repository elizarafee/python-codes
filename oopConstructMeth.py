# Class object attributes are the attributes which are defined at the beginning of a class openly.

class A():
    name = 'Tareque'

a = A()
print(a.name)



class Animal():
    species = 'mammal'

    # Constructor
    def __init__(altself, name, id):
        altself.perName = name
        altself.perId = id
    
    def color(altself, color):
        altself.perColor = color

    # Method and calling class attribute in method (Animal.species / altself.species) 
    def first_method(altself, tail):
        print("The species is {}, name is {}, color is {}, it has tail: {} ".format(Animal.species, altself.perName, altself.perColor, tail))

# creating object of a class, the attributes are assigned as they are mentioned in the constructor(__init__)
animal = Animal('puppy', 12)

# method's attribute is passed like this
animal.color('Blue')
animal.first_method(False)

# calling attributes 
print(animal.species)
print(animal.perName)