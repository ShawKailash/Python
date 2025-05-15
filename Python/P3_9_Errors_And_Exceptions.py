try:
    print("trying 1/0")
    total = 1/0
    print("this will not show up")
except Exception:
    print("exception was caught")
    total = 0
print(total)
print("\n")
num = input("what is a number: ")
try:
    num = int(num)
except Exception:
    num = "Unknown"
print(num)
