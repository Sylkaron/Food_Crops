from enum import Enum
import Describable
import Unit


class IndicatorGroup(Enum):
    EXPORTS_AND_IMPORTS = 3
    SUPPLY_AND_USE = 2
    PRICES = 1
    FEED_PRICES_RATIOS = 7
    QUANTITIES_FED = 6
    TRANSPORTATION = 4
    ANIMAL_UNIT_INDEXES = 5


class Indicator(Describable.Describable):

    def __init__(self, id: int, frequency: int, frequencyDesc: str, geogLocation: str, indicatorGroup: IndicatorGroup,
                 unit: Unit):
        super(Indicator, self).__init__()
        self.id = id
        self.__frequency = frequency
        self.__frequencyDesc = frequencyDesc
        self.__geogLocation = geogLocation
        self.indicatorGroup = indicatorGroup
        self.unit = unit

    def describe(self):
        a = "Indicator n° " + str(self.id) + " : " + str(self.indicatorGroup) + "\n frequence : "
        b = str(self.__frequency) + " " + self.__frequencyDesc + "\n Localisation : "
        c = self.__geogLocation + "\n Unit : " + self.unit.describe()
        return a + b + c
