import unittest
import greedy

class TestGreedy(unittest.TestCase):

    def test_greedy_single(self):
        self.assertEqual(greedy.greedy_multiple_knapsacks([10],[5,2,2],[10,20,8]), 38)

    def test_greedy_mutiple(self):
        self.assertEqual(greedy.greedy_multiple_knapsacks([10, 15],[5,2,24,4], [13,10,20,8]), 31)