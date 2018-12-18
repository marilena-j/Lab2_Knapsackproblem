import unittest
from random import Random
import neighborhood
import greedy

seed = 4523
generator = Random(seed)

def create_items(weights, values):
    return [ greedy.Item(values[i], weights[i]) for i in range(len(weights))]

def generate(num, min, max):
    return [generator.randint(min, max) for _ in range(num)]

class TestPerformance(unittest.TestCase):

    def test_100_20_random(self):
        values = generate(100, 1, 20)
        weights = generate(100, 1, 10)
        knapsacks = generate(20, 5, 15)

        result_greedy = greedy.greedy_multiple_knapsacks(knapsacks, create_items(values[:], weights[:]))
        result_neighborhood = neighborhood.neighborhoodSearch(weights, values[:], knapsacks[:])

        print(result_greedy, result_neighborhood)
