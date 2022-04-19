# -*- coding: utf-8 -*-
import unittest

from gilded_rose.gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_item_quality_cannot_be_negative(self):
        items = [Item("Elixir of the Mongoose", 3, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_item_quality_when_sell_in_expires(self):
        items = [Item("Elixir of the Mongoose", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(18, items[0].quality)


if __name__ == '__main__':
    unittest.main()
