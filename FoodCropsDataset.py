import pandas

class FoodCropsDataset:
    def __init__(self):

    def load(self, datasetPath: str):
        dataframe = pandas.read_csv(datasetPath)
        F = FoodCropFactory()
        for index, row in dataframe.iterrows():
            Prix = row["SC_Group_ID"] * 1000
            descPrix = row["SC_Group_Desc"]
            CommodityID =  row["SC_GroupCommod_ID"]
            CommodityDesc = row["SC_GroupCommod_Desc"]

    def findMeasurements(self, commodityType: CommodityType = None, indicatorGroup: IndicatorGroup = None,
                         geographicalLocation: str = None, unit: Unit = None):
        return