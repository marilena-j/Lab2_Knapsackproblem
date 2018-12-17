import unittest
import greedy

def create_items(weights, values):
    return [ greedy.Item(values[i], weights[i]) for i in range(len(weights))]

class TestGreedy(unittest.TestCase):

    def test_greedy_single(self):
        items = create_items([2,3,5,7,1,4,1], [10,5,15,7,6,18,3])
        result = greedy.greedy_multiple_knapsacks([15], items)
        self.assertEqual(result[0], 52)

    def test_greedy_mutiple(self):
        items = create_items([5,2,24,4], [13,10,20,8])
        result = greedy.greedy_multiple_knapsacks([10, 15], items)
        self.assertEqual(result[0], 31)