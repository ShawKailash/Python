def somename():
    print("hello world")
somename()
somename()
somename()
somename()
print("\n")

name="kailash"
def somenames():
    print(f"hello {name}")
somenames()
somenames()
print("\n")

def somename2(name):
    print(f"hello {name}")
somename2('karan')
print("\n")

def somename3(name, food):
    print(f"hello {name}. lets eat some {food}")
somename3('komal','pizza')
print("\n")

def somename3(name, food="mango"):
    if name.lower()=="komal":
        print("welcome komal")
    print(f"hello {name}. lets eat some {food}")
somename3('komal',food='orange')
print("\n")

def somefunction():
    return "a value"
thing=somefunction()
print(thing)
print("\n")

def exp(num1,num2):
    total=num1**num2
    return total
big_number=exp(2,4)
print(big_number)
