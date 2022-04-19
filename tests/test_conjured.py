import unittest

from gilded_rose.gilded_rose import Item, GildedRose


class ConjuredTest(unittest.TestCase):
    def test_conjured_sell_in(self):
        items = [Item("Conjured Mana Cake", 1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)

    def test_conjured_quality(self):
        items = [Item("Conjured Mana Cake", 1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(18, items[0].quality)


if __name__ == '__main__':
    unittest.main()
