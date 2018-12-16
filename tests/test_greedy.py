import unittest
import greedy

class TestGreedy(unittest.TestCase):

    def test_greedy_single(self):
        self.assertEqual(greedy.greedy_multiple_knapsacks([15],[2,3,5,7,1,4,1], [10,5,15,7,6,18,3]), 52)

    def test_greedy_mutiple(self):
        self.assertEqual(greedy.greedy_multiple_knapsacks([10, 15],[5,2,24,4], [13,10,20,8]), 31)