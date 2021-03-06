import pandas
from FoodCropFactory import *
from Indicator import *
from Commodity import *


class FoodCropsDataset:

    def __init__(self):
        self.F = FoodCropFactory()
        self.commodityGroupMeasurementIndex = dict()
        self.indicatorGroupMeasurementIndex = dict()
        self.locationMeasurementIndex = dict()
        self.unitMeasurementIndex = dict()

    def load(self, datasetPath: str):

        dataframe = pandas.read_csv(datasetPath)

        L = []
        for index, row in dataframe.iterrows():
            IndicatorID = row["SC_Group_ID"]
            groupCommodityID = row["SC_GroupCommod_ID"]
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

            if "ratio" in UnitDesc.lower():
                U = self.F.createRatio(UnitID)
            elif "dollar" or "euro" in UnitDesc.lower():
                U = self.F.createPrice(UnitID)
            elif "liter" or "Bushel" or "gallon" in UnitDesc.lower():
                U = self.F.createVolume(UnitID)
            elif "ton" in UnitDesc.lower():

                if "000" in UnitDesc.lower():
                    U = self.F.createWeight(UnitID, 1000)
                elif "Million" in UnitDesc.lower():
                    U = self.F.createWeight(UnitID, 1000000)
                else:
                    U = self.F.createWeight(UnitID, 1)
            elif "acre" in UnitDesc.lower():
                U = self.F.createSurface(UnitID)
            else:
                U = self.F.createCount(UnitID, UnitDesc)

            Ind = self.F.createIndicator(IndicatorID, FreqID, FreqDesc, GeographyDesc, IndicatorGroup(IndicatorID), U)

            if type(groupCommodityID) != int:
                groupCommodityID = 0

            G = self.F.createCommodity(CommodityGroup(groupCommodityID), groupCommodityID, groupCommodityDesc)

            M = self.F.createMeasurement(index, YearID, Amount, TimePID, TimePDesc, G, Ind)

            self.unitMeasurementIndex[index] = U
            self.locationMeasurementIndex[index] = GeographyDesc
            self.commodityGroupMeasurementIndex[index] = G
            self.indicatorGroupMeasurementIndex[index] = Ind

            L.append(M)

        return L

    def findmeasurements(self, commodityGroup: CommodityGroup = None, indicatorGroup: IndicatorGroup = None,
                         geographicalLocation: str = None, unit: Unit = None):
        indexG = []
        indexGI = []
        indexGIL = []
        indexGILU = []

        L = self.load(datasetPath="src/FeedGrains.csv")
        n = len(self.commodityGroupMeasurementIndex)

        for i in range(n):
            if self.commodityGroupMeasurementIndex[i] == commodityGroup:
                indexG.append(i)

        if len(indexG) > 0:
            for k in indexG:
                if self.indicatorGroupMeasurementIndex[k] == indicatorGroup:
                    indexGI.append(k)
        else:
            for k in range(n):
                if self.indicatorGroupMeasurementIndex[k] == indicatorGroup:
                    indexGI.append(k)

        if len(indexGI) > 0:
            for k in indexGI:
                if self.locationMeasurementIndex[k] == geographicalLocation:
                    indexGIL.append(k)
        else:
            for k in range(n):
                if self.locationMeasurementIndex[k] == geographicalLocation:
                    indexGIL.append(k)

        if len(indexGIL) > 0:
            for k in indexGIL:
                if self.unitMeasurementIndex[k] == unit:
                    indexGILU.append(k)
        else:
            for k in range(n):
                if self.unitMeasurementIndex[k] == unit:
                    indexGILU.append(k)

        if len(indexGILU) > 0:
            return [L[i] for i in indexGILU]

        else:
            return L
