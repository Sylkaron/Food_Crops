import Describable, Commodity, Indicator

class Measurement(Describable):
    def __init__(self, id: int, year: int, value: float, timeperiodld: int, timeperiodDesc: str,
                    commodity: Commodity, indicator: Indicator):
        self.year = year
        self.value = value
        self.timeperiodld = timeperiodld
        self.timeperiodDesc = timeperiodDesc


