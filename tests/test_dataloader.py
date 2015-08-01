# -*- coding: utf8 -*-
from trade.data.dataloader import DataLoader
import unittest


class TestDataLoader(unittest.TestCase):

    def testLoad(self):
        DataLoader().loadCSV("")

    def testStoreCSV(self):
        DataLoader().storeCSV("")
