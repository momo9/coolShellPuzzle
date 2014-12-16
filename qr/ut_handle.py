import unittest
from handle import *


class TestHandle(unittest.TestCase):

    def setUp(self):
        self.lut = genLut()

    def testTrans(self):
        self.assertEqual('a', transfer('p', self.lut))
        self.assertEqual('W', transfer('W', self.lut))
        self.assertEqual(',', transfer(',', self.lut))

    def testContent(self):
        self.assertEqual('is', transContent('ui', self.lut))


if __name__ == "__main__":
    unittest.main()
