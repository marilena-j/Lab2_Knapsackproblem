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

"""
It runnes neighborhood search algorithem N times. Each time it starts in a different
starting point. We return the best solution we find.
"""
def neighborhoodSearch(weights, values, knapsacks):
    value, solution = neighborhoodSearchIteration(weights, values, knapsacks)
    return value, solution

"""
One iteration of neighborhood search algorithem
It creates randomSolution and then using that builds a Neighborhood

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
