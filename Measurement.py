import Describable

class Measurement:
    def __init__(self, year: int, value: float, timeperiodld: int, timeperiodDesc: str):
        self.year = year
        self.value = value
        self.timeperiodld = timeperiodld
        self.timeperiodDesc = timeperiodDesc

    def measurement(self, id: int, year: int, value: float, timeperiodld: int, timeperiodDesc: str,
                    commodity: Commodity, indicator: Indicator ):

