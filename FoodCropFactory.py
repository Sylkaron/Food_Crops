from Indicator import *
from Unit import *
from Measurement import *
from Commodity import *


class FoodCropFactory:

    def __init__(self, ):
        self.__unitsRegistry = dict()
        self.__indicatorsRegistry = dict()
        self.__commodityRegistry = dict()

    def createVolume(self, id: int):
        if id not in self.__unitsRegistry:
            U = Unit.Volume(id)
            self.__unitsRegistry[id] = U
            return U
        else:
            return self.__unitsRegistry[id]

    def createPrice(self, id: int):
        if id not in self.__unitsRegistry:
            U = Unit.Price(id)
            self.__unitsRegistry[id] = U
            return U
        else:
            return self.__unitsRegistry[id]

    def createWeight(self, id: int, weight: float):
        if id not in self.__unitsRegistry:
            U = Unit.Weight(id, weight)
            self.__unitsRegistry[id] = U
            return U
        else:
            return self.__unitsRegistry[id]

    def createSurface(self, id: int):
        if id not in self.__unitsRegistry:
            U = Unit.Surface(id)
            self.__unitsRegistry[id] = U
            return U
        else:
            return self.__unitsRegistry[id]

    def createCount(self, id: int, what: str):
        if id not in self.__unitsRegistry:
            U = Unit.Count(id, what)
            self.__unitsRegistry[id] = U
            return U
        else:
            return self.__unitsRegistry[id]

    def createRatio(self, id: int):
        if id not in self.__unitsRegistry:
            U = Unit.Ratio(id)
            self.__unitsRegistry[id] = U
            return U
        else:
            return self.__unitsRegistry[id]

    def createCommodity(self, group: CommodityGroup, id: int, name: str):
        if id not in self.__commodityRegistry:
            C = Commodity.Commodity(group, id, name)
            self.__commodityRegistry[id] = C
            return C
        else:
            return self.__commodityRegistry[id]

    def createIndicator(self, id: int, frequency: int, freqDesc: str, geogLocation: str, indicatorGroup: IndicatorGroup,
                        unit: Unit):
        if id not in self.__indicatorsRegistry:
            Indic = Indicator.Indicator(id, frequency, freqDesc, geogLocation, indicatorGroup, unit)
            self.__indicatorsRegistry[id] = Indic
            return Indic
        else:
            return self.__indicatorsRegistry[id]

    def createMeasurement(self, id: int, year: int, value: float, timeperiodId: int, timeperiodDesc: str,
                          commodity: Commodity, indicator: Indicator):
        return Measurement.Measurement(id, year, value, timeperiodId, timeperiodDesc, commodity, indicator)
