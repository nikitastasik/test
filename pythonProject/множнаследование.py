class Animal:
    def die(self):
        print('bye-bye')
        self.health = 0

class Carnivour:
    def hunt(self):
        print('eating')
        self.satiely = 100

class Dog(Animal, Carnivour):
    def bark(self):
        print('woof-woof')
#
# dog = Dog()
# dog.bark()
# dog.hunt()
# dog.die()

class Animal:
    def set_health(self, health):
        print('set in animal')

class Carnivour(Animal):
    def set_health(self, health):
        print('set in carnivour')

class Mamal(Animal):
    def set_health(self, health):
        print('set in mamal')

class Dog(Mamal, Carnivour):
    pass


# dog2 = Dog()
# dog2.set_health(100)

class Animal:
    def set_health(self, health):
        print('set in animal')

class Carnivour(Animal):
    def set_health(self, health):
        super().set_health(health)
        # Animal.set_health(self, health)
        print('set in carnivour')

class Mamal(Animal):
    def set_health(self, health):
        super().set_health(health)
        # Animal.set_health(self, health)
        print('set in mamal')

class Dog(Mamal, Carnivour):
    def set_health(self, health):
        super().set_health(health)
        # Mamal.set_health(self, health)
        # Carnivour.set_health(self, health)


        print('set in dog')

dog3 = Dog()
dog3.set_health(10)
