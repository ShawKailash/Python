class Animal:
    for_color = "orange"

    def speak(self):
        raise NotImplementedError

    def eat(self):
        print("i am eating yum yum")
    
    def chase(self, animal="horse"):
        print("i am chasing a", animal)

class Housecat(Animal):
    def speak(self):
        print("meow")

    def eat(self):
        super().eat()
        print("i am eating food")

    def chase(self, animal):
        super().chase(animal)
        print(animal, "was caught")

cat = Housecat()
cat.eat()

cat.chase("mouse")
