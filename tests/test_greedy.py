import unittest
import greedy

class TestGreedy(unittest.TestCase):

    def test_greedy(self):
        self.assertEqual(greedy.greedy(), 0)
