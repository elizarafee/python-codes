# Jupytet Notebook can create file automaticaaly otherwise it need to be created manually

# %%writefile myfile.txt        	                    # creating file by jupyter notebook
# Hello this is a text file
# this is the second file
# this is the third file
# this is the fourth file

# Opening a existing file from directory
myfile = open('c:\\users\\hmtar\\myfile.txt')

print(myfile.read())                                    # printing file

print(myfile.read())                                    # printing file

myfile.seek(0)

print(myfile.read())

# PWD                                                   # getting the path directory we're in

with open('c:\\users\\hmtar\\my_new_file.txt', mode='r') as f:
    print(f.read())

# my_new_file.close()

# with open('c:\\users\\hmtar\\my_new_file.txt')    	# take the cursor after the 1st parethesis then tap
# (shift+tab)

with open('c:\\users\\hmtar\\my_new_file.txt', mode='a') as f:  # Adding contents by append 'a'
    f.write('this line is newly added')

with open('c:\\users\\hmtar\\my_new_file.txt', mode='r') as gg:
    print(gg.read())

# mode = 'r/ w/ rt/ wp'

# %%
