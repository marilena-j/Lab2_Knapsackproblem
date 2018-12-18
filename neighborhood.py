from random import Random
import numpy as np
import greedy

seed = 4523
generator = Random(seed)

"""
Evaluates a solution, calculates if it is valid and what is it's total value.
"""
def evaluate(solution, values, weights, knapsacks):
    totalValue = 0

    for knapsack in range(len(knapsacks)):
        weight = 0
        for i in range(len(solution)):
            if solution[i] == knapsack + 1:
                totalValue += values[i]
                weight += weights[i]

            if weight > knapsacks[knapsack]:
                return False, 0
        
    return True, totalValue

"""
It builds a neighborhood from a solution.
"""
def buildNeighborhood(solution, numOfKnap):
    solutions = []

    for i in range(len(solution)):
        solutions.append(solution[:])
        if solutions[i][i] >= numOfKnap:
            solutions[i][i] = 0
        else:
            solutions[i][i] += 1

    return solutions


def neighborhoodSearch(weights, values, knapsacks, method=''):
    if method == 'tabu':
        return neighborhoodSearchIterationTabu(weights, values, knapsacks)
    else:
        return neighborhoodSearchIteration(weights, values, knapsacks)

"""
One iteration of neighborhood search algorithm

When we have a neighborhood, we go through the solutions, if there is anyone
better than current global maximum, we set that solution as global maximum and create
another neighborhood from that and repeat the steps.
But, if in neighborhood there isn't any solution better than global maximum, then we break
and return the found global maximum.
"""
def neighborhoodSearchIteration(weights, values, knapsacks):
    globalMax = solutionFromGreedy(weights, values, knapsacks)
    _, globalMaxVal = evaluate(globalMax, values, weights, knapsacks)

    localMax = globalMax
    localMaxVal = globalMaxVal
    
    while True:
        neighborhood = buildNeighborhood(globalMax, len(knapsacks))

        for solution in neighborhood:
            valid, totalValue = evaluate(solution, values, weights, knapsacks)

            if valid and totalValue > localMaxVal:
                localMaxVal = totalValue
                localMax = solution

        if localMaxVal > globalMaxVal:
            globalMaxVal = localMaxVal
            globalMax = localMax
        else:
            break
    
    return globalMaxVal, globalMax

def neighborhoodSearchIterationTabu(weights, values, knapsacks):
    globalMax = solutionFromGreedy(weights, values, knapsacks)
    _, globalMaxVal = evaluate(globalMax, values, weights, knapsacks)

    tabu_list = []
    next_search_solution = globalMax
    
    for _ in range(len(weights)):
        neighborhood = buildNeighborhood(next_search_solution, len(knapsacks))
        found_at_least_one_not_tabu = False

        localMaxVal = -1
        localMax = None

        # Go through neigberhood and find a localMax, that's not in tabu
        for solution in neighborhood:
            valid, totalValue = evaluate(solution, values, weights, knapsacks)
            if solution not in tabu_list and valid:
                found_at_least_one_not_tabu = True
                if totalValue > localMaxVal:
                    localMaxVal = totalValue
                    localMax = solution

        # If all solutions in negberhood are in tabu, we break
        if not found_at_least_one_not_tabu:
            break

        # If local max is better than current global max, replace
        if localMaxVal > globalMaxVal:
            globalMaxVal = localMaxVal
            globalMax = localMax

        # Add local max to tabu list
        tabu_list = [localMax] + tabu_list[:-1]
        # When tabu list riches limit, we remove oldest element
        if len(tabu_list) >= 10:
            tabu_list = tabu_list[:-1]
    
    return globalMaxVal, globalMax

"""
Creates a random solution that we use as a starting point
"""
def randomSolution(numOfItems, numOfKnap):
    solution = []

    for i in range(numOfItems):
        solution.append(generator.randint(0, numOfKnap))

    return solution

"""
Create solution from a gready one
"""
def solutionFromGreedy(weights, values, knapsacks):
    items = [ greedy.Item(values[i], weights[i], i) for i in range(len(weights))]

    _, greedy_solution = greedy.greedy_multiple_knapsacks(knapsacks, items)

    solution = [ 0 for i in range(len(weights))]

    for i in range(len(greedy_solution)):
        for item in greedy_solution[i].items:
            solution[item.position] = i + 1

    return solution
