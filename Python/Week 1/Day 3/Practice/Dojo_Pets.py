class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name=first_name
        self.last_name=last_name
        self.treats=treats
        self.pet_food=pet_food
        self.pet=pet
    def walks(self):
        print(f"{self.first_name} is walking {self.pet}.")
        self.pet.play()
    def feed(self):
        print(f"{self.first_name} is feeding {self.pet}")
        self.pet.eat()
    def bathe(self):
        print(f"{self.first_name} is cleaning {self.pet}")
        self.pet.noise()
class pet:
    def __init__(self, name , type , tricks):
        self.name=name
        self.type=type
        self.tricks=tricks
        self.health= 100
        self.energy = 50
    def sleep(self):
        self.energy+= 25
        print(f"{self.name} is sleeping. Energy increased by 25")
    def eat(self):
        self.energy+= 5
        self.health+= 10
        print(f"{self.name} is eating. Energy is increased by  5 and his health is increased by 10 ")
    def play(self):
        self.health+= 5
        print(f"{self.name} is playing. Health is increased by 5")
    def noise(self):
        if self.type == "dog":
            print("Woof!")
        elif self.type == "cat":
            print("Meow!")
        else:
            print("Unknown pet type.")
pet1 = pet("Fluffy", "cat", ["roll over", "fetch"])
print("Initial Stats:")
print("Energy:", pet1.energy)
print("Health:", pet1.health)
pet1.sleep()
pet1.eat()
pet1.play()
print("Updated Stats:")
print("Energy:", pet1.energy)
print("Health:", pet1.health)
pet1.noise()