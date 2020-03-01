# Strings are ordered sequences. Means it can be INDEXED and SLICED to grab sub-section
# INDEXING notation uses []
# SLICING has a syntex [start. stop. step] start - starting, stop - go up to, step - size 
# The ways of formatting strings for printing variables is called interpolation.

a = 'Eliza Ahmed Rafee'
b = 'Hasan Mohammod Tareque '

print(b)
print(b[1], b[-1], a[-5])    # indexing/ reverrse indexing
print(b[2:])                 # 2nd index to last index
print(b[:3])                 # starting index to 2nd
print(b[1:3])                # index 1-2
print(b[::])                 # starting to ending
print(b[::1])   	         # index next to it
print(b[::2])                # next 2nd index next to it
print(b[2:12:2])    	     # from 2 to 11 with step size 2

# b[3] = 'e'                 # changing letters in this way is not acceptable in python
print('my nick name is ' + b[15:]) #Concatanation
print(b * 2)                 # multiplication of arrays

