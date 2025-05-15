class Animal:
    fur_color = "orange"

    def speak(self):
        print("kailash")

    def eat(self):
        pass
    
    def chase (self):
        pass

class Tiger(Animal):
    pass

class Housecat(Animal):
    fur_color = "black"
    def speak(self):
        print("meow")

tiger = Tiger()
tiger.speak()
print(type(tiger))
print(tiger.fur_color)

tiger = Animal()
tiger.speak()
print(type(tiger))

cat = Housecat()
cat.speak()
print(cat.fur_color)
