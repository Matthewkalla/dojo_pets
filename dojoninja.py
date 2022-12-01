from dojopet import Pet
class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet_name):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet(pet_name, 'dog', 'sit')

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        print(f"feeding {self.pet.name} a {self.pet_food}!")

    def bathe(self):
        print(f"Giving {self.pet.name} a bath!")
        self.pet.noise()
    