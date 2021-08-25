class Character():
    MAX_SPEED = 100

    def __init__(self, race, damage=10):
        self.__race = race
        self.damage = damage
        self._health = 100
        self.current_speed = 20

    def hit(self, damage):
        self._health -= damage
        print(self._health)

    @property
    def heath(self):
        return self._health

    @property
    def race(self):
        return self.__race

    @property
    def current_speed(self):
        return self.current_speed

    @current_speed.setter
    def current_speed(self, current_speed):
        if current_speed < 0:
            self.current_speed = 0
        elif current_speed > 100:
            self.current_speed = 100
        else:
            self.current_speed = current_speed




Character.MAX_SPEED = 200

print(Character.MAX_SPEED)


c = Character('Elf')
c.hit(10)
c.race()

# c._Character__race = 'Ork'
# print(c._Character__race)



c.current_speed = 1000
print(c.current_speed)