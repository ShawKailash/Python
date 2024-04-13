class Animal:
    for_color = "orange"

    def speak(self):
        raise NotImplementedError

    def eat(self):
        pass
    
    def chase (self):
        pass

class Housecat(Animal):
    def speak(self):
        print("meow")

cat = Housecat()
cat.speak()