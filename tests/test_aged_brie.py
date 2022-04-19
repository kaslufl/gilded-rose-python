import unittest

from gilded_rose.gilded_rose import Item, GildedRose


class AgedBrieTest(unittest.TestCase):
    def test_aged_brie_quality(self):
        items = [Item("Aged Brie", 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_aged_brie_sell_in(self):
        items = [Item("Aged Brie", 1, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(50, items[0].quality)


if __name__ == '__main__':
    unittest.main()
