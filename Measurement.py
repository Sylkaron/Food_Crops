import Commodity
import Describable
import Indicator


class Measurement(Describable.Describable):
    def __init__(self, id: int, year: int, value: float, timeperiodld: int, timeperiodDesc: str,
                 commodity: Commodity, indicator: Indicator):
        super(Measurement, self).__init__()
        self.id = id
        self.__year = year
        self.__value = value
        self.__timeperiodld = timeperiodld
        self.__timeperiodDesc = timeperiodDesc
        self.commodity = commodity
        self.indicator = indicator

    def describe(self):
        return "Measure n° " + str(self.id) + "\n Periode : " + str(self.__timeperiodDesc) + str(self.__year) + "\n" + self.commodity.describe() + "\n" + self.indicator.describe()+ "\n Value : " + str(self.__value) + "\n"
