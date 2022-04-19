import unittest

from gilded_rose.gilded_rose import Item, GildedRose


class SulfurasTest(unittest.TestCase):
    def test_sulfuras_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)

    def test_sulfuras_sell_in(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)  # add assertion here


if __name__ == '__main__':
    unittest.main()
