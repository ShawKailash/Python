def person(**kwargs):
    print(kwargs)
    print(type(kwargs))

    if 'age' in kwargs:
        print("you are is", kwargs.get("age"))

person(name="kailash", age=24, brain="learn")

def order(name, address, **toppings):
    print(f"order is for {name}")
    print(f"ship is for {address}")
    price = 10.00

    for key, value in toppings.items():
        price = price+2.00
    print(f"the total price is {price}")
    return price
total=order("kailash","ranchi",jalapenos=True,extra_cheese=True,ham=True)
