# -*- coding: utf8 -*-
from pulsar import get_event_loop, new_event_loop
import unittest


class TestEventLoop(unittest.TestCase):

    def testLoop(self, loop=None):
        self._loop = loop or get_event_loop() or new_event_loop()
