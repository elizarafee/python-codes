# generator functions allows us to write a function that can send back a value and then later resume to pick up where it left off
# generator allows us to generate sequence of values over time
# the main difference in syntex will be the use of a yeild statement
# when na generator function is explained they become an OBJECT that supports an iteration protocol

# normal
def normal_func(a):
    b = []
    for x in range(a):
        b.append(x*3)
    return b

for x in normal_func(4):
    print(x)

# generator function(yield)
def generator_func(a):
    for x in range(a):
        yield x**3

for x in generator_func(10):
    print(x)

print(list(generator_func(3)))