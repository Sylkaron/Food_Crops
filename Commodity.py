from enum import Enum

import Describable


class CommodityGroup(Enum):
    CORN = 1
    BARLEY = 2
    OATS = 3
    SORGHUM = 4
    BYPRODUCT_FEEDS = 5
    COARSE_GRAINS = 6
    HAY = 7
    FEED_GRAINS = 8
    ANIMAL_PROTEIN_FEEDS = 9
    GRAIN_PROTEIN_FEEDS = 10
    PROCESSED_FEEDS = 11
    ENERGY_FEEDS = 12
    OTHER = 13


class Commodity(Describable):
    def __init__(self, group: CommodityGroup, id: int, name: str):
        super(Commodity, self).__init__()
        self.id = id
        self.name = name
        self.group = group
