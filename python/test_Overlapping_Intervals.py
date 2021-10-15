import unittest
from Overlapping_Intervals import my_fun, overlaps


class TestMyFun(unittest.TestCase):
    def test_my_fun(self):
        self.assertEqual(my_fun([(1, 3), (5, 8), (4, 10), (20, 25)]), [(1, 3), (4, 10), (20, 25)])




class TestOverlaps(unittest.TestCase):
    def test_overlaps(self):
        self.assertEqual(overlaps((1, 3), (2, 4)), (1, 4))
        self.assertEqual(overlaps((3, 7), (4, 6)), (3, 7))
        self.assertEqual(overlaps((3, 7), (2, 8)), (2, 8))
        self.assertEqual(overlaps((1, 3), (5, 8)), False)
