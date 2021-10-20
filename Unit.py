from abc import ABC
import Describable


class Unit(ABC, Describable):
    def __init__(self, id: int, name: str):
        super(Unit, self).__init__()
        self.id = id
        self.name = name


class Volume(Unit):
    def __init__(self, id: int, multiplier: float, name: str = 'Volume'):
        super(Volume, self).__init__(id, name)
        self.__multiplier = multiplier


class Price(Unit):
    def __init__(self, id: int, name: str = 'Price'):
        super(Price, self).__init__(id, name)


class Weight(Unit):
    def __init__(self, id: int, multiplier: float, name: str = 'Weight'):
        super(Weight, self).__init__(id, name)
        self.__multiplier = multiplier


class Surface(Unit):
    def __init__(self, id: int, multiplier: float, name: str = 'Surface'):
        super(Surface, self).__init__(id, name)
        self.multiplier = multiplier


class Count(Unit):
    def __init__(self, id: int, what: str, name: str = 'Count'):
        super(Count, self).__init__(id, name)
        self.__what = what
