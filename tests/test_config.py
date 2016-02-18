# -*- coding: utf8 -*-

import unittest
import io
from os.path import isfile

import goodtrader.common.configure as conf


class TestConfig(unittest.TestCase):

    def setUp(self):
        self.bak = conf.DB_CONNECT_STRING

    def tearDown(self):
        conf.DB_CONNECT_STRING = self.bak

    def testDefaultDbConStr(self):
        if not isfile(conf.CONFIG_PATH):
            self.assertEqual(
                conf.DB_CONNECT_STRING, "postgresql+psycopg2://localhost/trading")

    def testDbConStr(self):
        conf_str = "DB_CONNECT_STRING: test"
        conf._load_config(io.StringIO(conf_str))
        self.assertEqual(conf.DB_CONNECT_STRING, "test")
