def thing1():
    print("welcome to thing 1")
    def thing2():
        print("welcome to thing 2")
    thing2()
thing1()
print("\n")

def thing1(name):
    print("welcome to thing 1",name)
    def thing2():
        print("welcome to thing 2",name)
    thing2()
thing1("kailash")