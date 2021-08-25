# class Character:
#
#     def __init__(self):
#         self.race = 'Elf'



class Character:

    _instance = None

    def __next__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.race = 'Elf'

c = Character()
d = Character()
d.race = 'Ork'
f = Character()
print(c.race)
print(d.race)
print9
