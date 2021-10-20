import pandas


class FoodCropsDataset:
    def __init__(self):

    def load(self, datasetPath: str):
        dataset = pandas.read_csv(datasetPath)

    def findMeasurements(self, commodityType: CommodityType = None, indicatorGroup: IndicatorGroup = None,
                         geographicalLocation: str = None, unit: Unit = None):
        return