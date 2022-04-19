from gilded_rose import Item

EXPIRED_VALUE = 0
INCREASE_RATE = 1
DECREASE_RATE = 1
MAX_QUALITY = 50
MIN_QUALITY = 0


class GildedRose(object):
    items: list[Item]

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > MIN_QUALITY:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - DECREASE_RATE
            else:
                if item.quality < MAX_QUALITY:
                    item.quality = item.quality + INCREASE_RATE
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < MAX_QUALITY:
                                item.quality = item.quality + INCREASE_RATE
                        if item.sell_in < 6:
                            if item.quality < MAX_QUALITY:
                                item.quality = item.quality + INCREASE_RATE
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - DECREASE_RATE
            if item.sell_in < EXPIRED_VALUE:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > MIN_QUALITY:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - DECREASE_RATE
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < MAX_QUALITY:
                        item.quality = item.quality + INCREASE_RATE
