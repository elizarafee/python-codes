# The ways of formatting strings for printing variables is called interpolation.
# Two available ways of doing are : format() & f-strings

print('This is a string {}'.format('took from format method'))
print('serials : {} {} {}'.format('A', 'B', 'C'))
print('serials : {b} {c} {a}'.format(a='Aaa', b='Bbb', c='Ccc'))
print('{1} {0} {2}'.format('Mohammod', 'Hasan', 'Tareque'))

result = 10/2
print('the result was {}'.format(result))
print('the result was {r}'.format(r = result))
number = 123456.123456
print("the result was {num:3.3f}".format(num = number))
print("the result was {num:1.5f}".format(num = number))

first_name = 'Hasan'
last_name = 'Tareque'
print(f'Hi Mr {first_name} {last_name}')

print("i'm going to inject %s here"%'something')
print("i'm going to use it twice: %s %s"%('FIRST', 'SECOND'))
x, y = 'here', 'there'
print("i'm going to inject something %s and %s"%(x, y))

print("i'm going to inject something %2.3f"%(12345.12345))
print("i'm going to inject something %15.3f"%(12345.12345))

# %r??