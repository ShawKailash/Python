can_code=True
if can_code==True:
    print("you can code")
else:
    print("you dont know how to code yet")
print("\n")

teacher = "Kailash"
if teacher.lower()== "kailash":
    print("you are teacher")
else:
    print("you are a student")
print("\n")

name = input("what is your name ")
if name == "Bob":
    print("welcome Bob")
    bring_food = "pizza"
elif name=="kailash":
    print("welcome kailash")
    bring_food="milk"
elif name=="karan":
    print("welcome karan")
    bring_food="chicken"
else:
    print("welocme another")
    bring_food = "mango"
print(f"you are eating {bring_food}")
print("\n")

name = input("what is your name ")
name = name.lower()
if name!="bob":
    print("you are not bob get you here")
else:
    print("welcome bobby boy")
print("\n")

age=input("your age is ")
age=int(age)
if age==18:
    print("you are come to party")
elif age<=18:
    print("you are not come to party")
elif age<=40:
    print("you are come to party")
elif age>=40:
    print("you are not come to party")