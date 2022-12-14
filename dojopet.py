class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        print(f"{self.name} enjoys a walk!")
        return self

    def noise(self):
        if self.type == "dog":
            print(f"{self.name} barks with enjoyment!")
        else:
            print(f"{self.name} meows in protest!")
        return self
