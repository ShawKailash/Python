def myfunc():
    for num in range(14):
        print(num)
    
myfunc()

def myfunc():
    for num in range(14):
        return num ** num
    
total = myfunc()
print(total)

def myfunc():
    for num in range(14):
        yield num ** num
    
total = myfunc()
print(total)

def myfunc():
    for num in range(14):
        yield 14 ** 14
    
total = myfunc()
print(total)

def my_generator():
    for num in range(14):
        yield num ** num

for big_num in my_generator():
    print(big_num)

all_numbers = list(my_generator())
print(all_numbers)

total = list(range(14))
print(total)

def my_generator():
    for num in range(14):
        yield num ** num

for big_num in my_generator():
    print(big_num)

my_var_gen = my_generator()
all_numbers = list(my_var_gen)
print(all_numbers)
