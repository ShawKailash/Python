class Animal:

    animal_type = "Unknown"

    def __init__(self, fur_color):
        print(f"fur color is {fur_color}")
        self.fur_color = fur_color

    def speak(self):
        raise NotImplementedError

    def eat(self):
        print("i am eating yum yum")
    
    def chase(self, animal="horse"):
        print("i am chasing a", animal)

    def get_fur_color(self):
        print("getting fur color is", self.fur_color)

class Housecat(Animal):

    def __init__(self, fur_color):
        super().__init__(fur_color)
        print("fur color was saved to the class object")
        self.animal_type = "House cat"
        print(self.animal_type)

    def speak(self):
        print("meow")

    def eat(self):
        super().eat()
        print("i am eating food")

    def chase(self, animal):
        super().chase(animal)
        print(animal, "was caught")

cat = Housecat("orange")
cat.eat()

cat.chase("mouse")
cat.get_fur_color()
