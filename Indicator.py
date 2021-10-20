from enum import Enum
import Describable

class IndicatorGroup(Enum):
    EXPORTS_AND_IMPORTS = 1



class Indicator():

    def __init__(self,id: str,frequency: int,frequencyDesc:str,geogLocation:str):
        self.id = id
        self.frequency = frequency
        self.frequencyDesc = frequencyDesc
        self.geogLocation = geogLocation

    def Indicator(id:int,frequency:int,freqDesc:str,geogLocation:str,indicatorGroup:IndicatorGroup,unit:Unit):



