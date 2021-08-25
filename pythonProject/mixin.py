class Vehicle:

    def __init__(self, position):
        self.position = position

    def travel(self, destination):
        route = calculate_route(source=self.position, to = destination)
        self.move_along(route)

    def calculate_route(self, source, to):
        return 0

    def move_along(self, route):
        print('moving')

class Car(Vehicle):
    pass

class Airplane(Vehicle):
    pass

class RadioMixin:

    def __init__(self):
        self.radio = Radio()

    def turn_on(self, station):
        self.radio.set_station(station)
        self.radio.play()

class Radio:
    def set_station(self, station):
        self.station = station

    def play(self):
        print(f'playing {self.station}')

class Car(Vehicle, RadioMixin):

    def __init__(self):
        Vehicle.__init__(self, (10, 20))
        RadioMixin.__init__(self)

car = Car()
car.turn_on('Moscow FM')

class ToDictMixin(object):
    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        return output

    def _traverse(self, key, value):
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value


class BinaryTree(ToDictMixin):

    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

tree = BinaryTree(10,
                  left = BinaryTree(7, right = BinaryTree(9)),
                  right = BinaryTree(12, left = BinaryTree(11)))

print(tree.to_dict())