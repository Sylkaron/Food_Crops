import Unit, Indicator, Measurement

class FoodCropFactory():

    def __init__(self):
        pass

    def createVolume(self, id:int):
        return Volume(id)

    def createPrice(self, id:int):
        return Price(id)

    def createWeight(self, id:int, weight:float):
        return Weight(id,weight)

    def createSurface(self, id:int):
        return Surface(id)

    def createCount(self,id:int, what:str):
        return Count(id, what)

    def createRatio(self, id:int):
        return Ratio(id)

    def createCommodity(self, group:CommodityGroup, id:int, name:str):
        new Commodity(group, id, name)

    def createIndicator(self, id:int, frequency:int, freqDesc:str, geogLocation:str, indicatorGroup:IndicatorGroup, unit:Unit ):
        return Indicator(id, frequency, freqDesc, geogLocation, indicatorGroup, unit)

    def createMeasurement(self, id:int, year:int, value:float, timeperiodId:int, timeperiodDesc:str, commodity:Commodity, indicator:Indicator):
        return Measurement(id, year, value, timeperiodId, timeperiodDesc, commodity, indicator)
