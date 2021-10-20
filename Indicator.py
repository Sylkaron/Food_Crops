from enum import Enum
import Describable

class IndicatorGroup(Enum):
    EXPORTS_AND_IMPORTS = 1
    SUPPLY_AND_USE = 2
    PRICES = 3
    FEED_PRICES_RATIOS = 4
    QUANTITIES_FED=5
    TRANSPORTATION=6
    ANIMAL_UNIT_INDEXES = 7



class Indicator(Describable):

    def __init__(self,id: str,frequency: int,frequencyDesc:str,geogLocation:str,indicatorGroup:IndicatorGroup,unit:Unit):
        super(Indicator, self).__init__()
        self.id = id
        self.frequency = frequency
        self.frequencyDesc = frequencyDesc
        self.geogLocation = geogLocation
        self.indicatorGroup = indicatorGroup
        self.unit = unit
        




