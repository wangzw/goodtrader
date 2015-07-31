import unittest

from trade.demo import echo

class TestEcho(unittest.TestCase):
    
    def testHi(self):
        d = echo("hello world\n")
        self.failUnlessEqual("hello world\n", d.hi())
