from enum import Enum

import Describable


class CommodityGroup(Enum):
    CORN = 12
    BARLEY = 9
    OATS = 17
    SORGHUM = 20
    BYPRODUCT_FEEDS = 10
    COARSE_GRAINS = 11
    HAY = 16
    FEED_GRAINS = 14
    ANIMAL_PROTEIN_FEEDS = 8
    GRAIN_PROTEIN_FEEDS = 15
    PROCESSED_FEEDS = 19
    ENERGY_FEEDS = 13
    OILSEED_MEAL_FEEDS = 18


class Commodity(Describable.Describable):
    def __init__(self, group: CommodityGroup, id: int, name: str):
        super(Commodity, self).__init__()
        self.id = id
        self.__name = name
        self.group = group

    def describe(self):
        return "Commodity n° : " + str(self.id) + "\n nom = " + self.__name
