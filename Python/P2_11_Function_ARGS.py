def addnumber(*args):
    print(args)
    print(type(args))
    total=0
    for num in args:
        total=total+num
    return total

total=addnumber(1,3,5,7,9)
print(total)