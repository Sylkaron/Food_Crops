import Commodity
import Describable
import Indicator


class Measurement(Describable):
    def __init__(self, id: int, year: int, value: float, timeperiodld: int, timeperiodDesc: str,
                 commodity: Commodity, indicator: Indicator):
        super(Measurement, self).__init__()
        self.year = year
        self.value = value
        self.timeperiodld = timeperiodld
        self.timeperiodDesc = timeperiodDesc
        self.commodity = commodity
        self.indicator = indicator
