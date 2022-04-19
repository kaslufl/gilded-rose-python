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
        if self.is_decrementable(item):
            self.adjust_quality(DECREASE_RATE, item)
        else:
            if item.quality < MAX_QUALITY:
                multiplier = self.increase_multiplier(item)
                self.adjust_quality(INCREASE_RATE * multiplier, item)

        if item.name != ItemEnum.SULFURAS.value:
            self.adjust_sell_in(DECREASE_RATE, item)

        if self.is_item_expirable(item):
            if item.name != ItemEnum.AGED_BRIE.value:
                if item.name != ItemEnum.BACKSTAGE_PASS.value:
                    if item.name != ItemEnum.SULFURAS.value:
                        self.adjust_quality(DECREASE_RATE, item)
                else:
                    item.quality -= item.quality
            else:
                if item.quality < MAX_QUALITY:
                    self.adjust_quality(INCREASE_RATE, item)

    def is_item_expirable(self, item):
        return item.sell_in < EXPIRED_VALUE

    def is_decrementable(self, item):
        return item.name != ItemEnum.AGED_BRIE.value and item.name != ItemEnum.BACKSTAGE_PASS.value \
               and item.name != ItemEnum.SULFURAS.value

    def adjust_sell_in(self, adjust, item):
        item.sell_in = item.sell_in + adjust

    def adjust_quality(self, adjust, item):
        if item.quality > MIN_QUALITY:
            item.quality = item.quality + adjust

        if item.quality > MAX_QUALITY:
            item.quality = MAX_QUALITY

    def increase_multiplier(self, item):
        multiplier = 1
        if item.name == ItemEnum.BACKSTAGE_PASS.value:
            if item.sell_in < 11:
                multiplier += 1
            if item.sell_in < 6:
                multiplier += 1
        return multiplier
