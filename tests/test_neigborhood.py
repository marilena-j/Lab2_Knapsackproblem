import unittest
import neighborhood

class TestNeighborhood(unittest.TestCase):

    def test_neighborhood_single(self):
        result = neighborhood.neighborhoodSearch([2,3,5,7,1,4,1], [10,5,15,7,6,18,3], [15])
        print()
        print(result)
        print()
        self.assertEqual(result[0], 52)

    def test_neighborhood_mutiple(self):
        result = neighborhood.neighborhoodSearch([5,2,24,4], [13,10,20,8], [10, 15])
        self.assertEqual(result[0], 31)