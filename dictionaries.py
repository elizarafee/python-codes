# Dictionaries are unordered mapping for storing objects
# dictionaries uses a key-value pairing instead, this allows a user to quickly grab objects without its index loc
# Dictionaries can't be sliced and indexed 
# Dictionaries can hold lists and another dictionaries in it
# ex : 
# dictionary = { 
#       'key1' : 'value1',
#       'key2' : 'value2'
# }

my_dict = {
    'k1' : 100,
    'k2' : 200.50,
    'k3' : 300,
    'k4' : 400
}

print(my_dict)
print(my_dict['k1'])

new_dict = {
    'k1' : 100,
    'k2' : 200.50,
    'k3' : 'Hasan Mohammad Tareque',
    'k4' : [0,1,2,3],
    'k5' : {
        'k6' : '300',
        'k7' : 'Eliza Ahmed Rafee' 
    },
    'k8' : 100
}
print(new_dict)
print(new_dict['k4'][1])                            
print(new_dict['k5']['k6'])


my_dictionary = {
    'k1' : [1, 2, 3, 4],
    'k2' : 200,
    'k3' : 300,
    'k4' : 400
}

my_list = my_dictionary['k1']
my_number = my_dictionary['k2']
print(my_list, my_number)

my_dictionary['k1'] = 100             	        # chananging value
print(my_dictionary)
print(my_dictionary.keys())                     # getting keys from dictionaries
print(my_dictionary.values())                   # getting values from dictionaries
print(my_dictionary.items())                    # getting items from dictionaries