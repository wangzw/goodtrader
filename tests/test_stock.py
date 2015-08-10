# -*- coding: utf8 -*-
from goodtrader.data.stock import Stock
import unittest


class TestStock(unittest.TestCase):

    def testInit(self):
        self.assertEqual("", Stock().name)
        self.assertEqual("", Stock().id)
