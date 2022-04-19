# -*- coding: utf-8 -*-
import unittest

from gilded_rose.gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)

    #todo: conjured test


if __name__ == '__main__':
    unittest.main()
