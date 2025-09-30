class Animal():
    zoo_name = "Marand_zoo"

    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def __str__(self):
        return f"{self.name}, {self.species}, {self.age}, {self.sound}"
    
    def make_sound(self):
        return f"{self.name} says {self.sound}"
    
    def info(self):
        return (f"Name : {self.name} \n"
                f"Species : {self.species}\n"
                f"age : {self.age}\n"
                f"sound : {self.sound}\n"
                f"zoo : {Animal.zoo_name}\n"             
    )
    
lion = Animal("simba", "lion", 5, "roar")


class Bird(Animal):
    def __init__(self, name, species, age, sound, wing_span):
        super().__init__(name, species, age, sound)
        self.wing_span = wing_span

        
parrot = Bird("karim", "parrot", 2, "squawk", 25)

print(lion)
print(lion.make_sound())
print(lion.info())
print(parrot.info())
print(parrot.wing_span)