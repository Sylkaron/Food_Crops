from enum import Enum
import Describable
import Unit


class IndicatorGroup(Enum):
    EXPORTS_AND_IMPORTS = 1
    SUPPLY_AND_USE = 2
    PRICES = 3
    FEED_PRICES_RATIOS = 4
    QUANTITIES_FED = 5
    TRANSPORTATION = 6
    ANIMAL_UNIT_INDEXES = 7


class Indicator(Describable):

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
        return "Indicator n° : " + str(self.id) + "\n frequence : " + str(self.__frequency) + " " + self.__frequencyDesc + "\n Localisation : "+self.__geogLocation + "\n Unit : " + self.unit.describe()
