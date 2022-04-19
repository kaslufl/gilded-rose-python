from gilded_rose import Item, ItemEnum

EXPIRED_VALUE = 0
INCREASE_RATE = 1
DECREASE_RATE = -1
MAX_QUALITY = 50
MIN_QUALITY = 0


class GildedRose(object):
    items: list[Item]

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.update_item(item)

    def update_item(self, item):
        if item.name != ItemEnum.AGED_BRIE.value and item.name != ItemEnum.BACKSTAGE_PASS.value:
            if item.quality > MIN_QUALITY:
                if item.name != ItemEnum.SULFURAS.value:
                    item.quality = self.adjust_quality(DECREASE_RATE, item)
        else:
            if item.quality < MAX_QUALITY:
                item.quality = self.adjust_quality(INCREASE_RATE, item)
                if item.name == ItemEnum.BACKSTAGE_PASS.value:
                    if item.sell_in < 11:
                        if item.quality < MAX_QUALITY:
                            item.quality = self.adjust_quality(INCREASE_RATE, item)
                    if item.sell_in < 6:
                        if item.quality < MAX_QUALITY:
                            item.quality = self.adjust_quality(INCREASE_RATE, item)
        if item.name != ItemEnum.SULFURAS.value:
            item.sell_in = self.adjust_sell_in(DECREASE_RATE, item)
        if item.sell_in < EXPIRED_VALUE:
            if item.name != ItemEnum.AGED_BRIE.value:
                if item.name != ItemEnum.BACKSTAGE_PASS.value:
                    if item.quality > MIN_QUALITY:
                        if item.name != ItemEnum.SULFURAS.value:
                            item.quality = self.adjust_quality(DECREASE_RATE, item)
                else:
                    item.quality = item.quality - item.quality
            else:
                if item.quality < MAX_QUALITY:
                    item.quality = self.adjust_quality(INCREASE_RATE, item)

    def adjust_sell_in(self, adjust, item):
        return item.sell_in + adjust

    def adjust_quality(self, adjust, item):
        return item.quality + adjust
