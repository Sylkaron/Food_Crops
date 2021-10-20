import Commodity
import Describable
import Indicator


class Measurement(Describable):
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
