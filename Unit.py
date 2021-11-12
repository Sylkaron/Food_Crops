import Describable


class Unit(Describable.Describable):
    def __init__(self, id: int, name: str):
        super(Unit, self).__init__()
        self.id = id
        self.name = name

    def describe(self):
        return "Unit ID : "+str(self.id)+"\n"+self.name


class Volume(Unit):
    def __init__(self, id: int, name: str = 'Volume'):
        super(Volume, self).__init__(id, name)


class Price(Unit):
    def __init__(self, id: int, name: str = 'Price'):
        super(Price, self).__init__(id, name)


class Weight(Unit):
    def __init__(self, id: int, multiplier: float, name: str = 'Weight'):
        super(Weight, self).__init__(id, name)
        self.__multiplier = multiplier

    def describe(self):
        return "Unit ID : "+str(self.id)+"\n"+self.name + "\n Multiplier : " + str(self.__multiplier)


class Surface(Unit):
    def __init__(self, id: int, name: str = 'Surface'):
        super(Surface, self).__init__(id, name)


class Count(Unit):
    def __init__(self, id: int, what: str, name: str = 'Count'):
        super(Count, self).__init__(id, name)
        self.__what = what

    def describe(self):
        return "Unit ID : "+str(self.id)+"\n"+self.name + "\n Objets : " + str(self.__what)


class Ratio(Unit):
    def __init__(self, id: int, name: str = 'Ratio'):
        super(Ratio, self).__init__(id, name)
