import pandas
from FoodCropFactory import *


class FoodCropsDataset:

    def __init__(self):
        self.F = FoodCropFactory()
        self.commodityGroupMeasurementIndex = dict()
        self.indicatorGroupMesurementIndex = dict()
        self.locationMeasurementIndex = dict()
        self.unitMesurementIndex = dict()

    def load(self, datasetPath: str):
        dataframe = pandas.read_csv(datasetPath)
        for index, row in dataframe.iterrows():
            IndicatorID = row["SC_Group_ID"] * 1000
            IndicatorDesc = row["SC_Group_Desc"]
            groupCommodityID =  row["SC_GroupCommod_ID"]
            groupCommodityDesc = row["SC_GroupCommod_Desc"]
            GeographyID = row["SC_Geography_ID"]
            SortOrder = row["SortOrder"]
            GeographyDesc = row["SC_GeographyIndented_Desc"]
            Commodity = row["SC_Commodity_ID"]
            CommodityDesc = row["SC_Commodity_Desc"]
            AttributeID = row["SC_Attribute_ID"]
            AttributeDesc = row["SC_Attribute_Desc"]
            UnitID = row["SC_Unit_ID"]
            UnitDesc = row["SC_Unit_Desc"]
            YearID = row["Year_ID"]
            FreqID = row["SC_Frequency_ID"]
            FreqDesc = row["SC_Frequency_Desc"]
            TimePID = row["Timeperiod_ID"]
            TimePDesc = row["Timeperiod_Desc"]
            Amount = row["Amount"]

            if "per" or "ratio"  in UnitDesc.lower():
                U = F.createRatio(UnitID)
            elif "dollar" or "euro" in UnitDesc.lower():
                U = F.createPrice(UnitID)
            elif "liter" or "Bushel" or "gallon" in UnitDesc.lower():
                U = F.createVolume(UnitID)
            elif "ton" in UnitDesc.lower():
                U = F.createWeight(UnitID, UnitDesc)
            elif "acre" in UnitDesc.lower():
                U = F.createSurface(UnitID)
            else :
                U = F.createCount(UnitID,UnitDesc)

            I = F.createIndicator(IndicatorID, FreqID, FreqDesc, GeographyDesc, groupCommodityID, U)

            G = F.createCommodity(groupCommodityID, groupCommodityDesc)

            M = F.createMeasurement(index, YearID, Amount, timeperiodId, timeperiodDesc, G, I)

            self.unitMesurementIndex[index] = U
            self.locationMeasurementIndex[index] = GeographyDesc
            self.commodityGroupMeasurementIndex[index] = G
            self.indicatorGroupMesurementIndex[index] = I

    def findMeasurements(self, commodityType: CommodityType = None, indicatorGroup: IndicatorGroup = None,
                         geographicalLocation: str = None, unit: Unit = None):
        return