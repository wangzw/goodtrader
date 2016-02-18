# -*- coding: utf8 -*-

import unittest

from goodtrader.data.stock import *


class TestStock(unittest.TestCase):

    def testCompany(self):
        self.assertEqual("Google (GOOG)", str(Company("Google", "GOOG")))
