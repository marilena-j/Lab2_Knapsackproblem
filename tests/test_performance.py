import unittest
from random import Random
import neighborhood
import greedy

seed = 4523
generator = Random(seed)

def create_items(weights, values):
    return [ greedy.Item(values[i], weights[i], i) for i in range(len(weights))]

def generate(num, min, max):
    return [generator.randint(min, max) for _ in range(num)]

class TestPerformance(unittest.TestCase):

    def test_100_20_random(self):
        values = generate(100, 1, 20)
        weights = generate(100, 1, 10)
        knapsacks = generate(20, 5, 15)

        value_greedy, _ = greedy.greedy_multiple_knapsacks(knapsacks, create_items(values[:], weights[:]))
        value_neighborhood, _ = neighborhood.neighborhoodSearch(weights, values[:], knapsacks[:])
        value_neighborhood_tabu, _ = neighborhood.neighborhoodSearch(weights, values[:], knapsacks[:], 'tabu')

        print(value_greedy, value_neighborhood, value_neighborhood_tabu)
        self.assertGreaterEqual(value_neighborhood, value_greedy)


    def test_1000_200_random(self):
        values = generate(1000, 1, 20)
        weights = generate(1000, 1, 10)
        knapsacks = generate(200, 5, 15)

        value_greedy, _ = greedy.greedy_multiple_knapsacks(knapsacks, create_items(values[:], weights[:]))
        value_neighborhood, _ = neighborhood.neighborhoodSearch(weights, values[:], knapsacks[:])
        value_neighborhood_tabu, _ = neighborhood.neighborhoodSearch(weights, values[:], knapsacks[:], 'tabu')

        print(value_greedy, value_neighborhood, value_neighborhood_tabu)
        self.assertGreaterEqual(value_neighborhood, value_greedy)
