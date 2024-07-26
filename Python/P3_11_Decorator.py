def my_decorator(func):
    def wrapper():
        print("do something here")
        func()
        print("original function is finished")
    return wrapper

@my_decorator
def myfunc():
    print("my name is kailash")
    
myfunc()