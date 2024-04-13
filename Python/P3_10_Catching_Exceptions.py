num = input("what is a number: ")
try:
    num = int(num)
except Exception:
    num = "Unknown"
print(num)
print("\n")

num = input("what is a number: ")
try:
    num = int(num)
except Exception as e:
    print("exception was caught")
    print(type(e))
    num = "Unknown"
print(num)
print("\n")

num = input("what is a number: ")
try:
    num = int(num)
except ValueError:
    print(num,"was not a valid number")
except Exception as e:
    print("exception was caught")
    print(type(e))
    num = "Unknown"
print(num)
print("\n")

num1 = input("what is a 1 number: ")
num2 = input("what is a 2number: ")
try:
    num1 = int(num1)
    num2 = int(num2)
    total = num1/num2
except ValueError:
    print(num,"was not a valid number")
except ZeroDivisionError:
    print("number could not be divided")
except Exception as e:
    print("exception was caught")
    print(type(e))
    num = "Unknown"