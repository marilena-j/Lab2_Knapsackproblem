from random import Random
import numpy as np

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
    bestSolutionValue, bestSolution, bestSolutionValid = neighborhoodSearchIteration(weights, values, knapsacks)

    for _ in range(5000):
        value, solution, valid = neighborhoodSearchIteration(weights, values, knapsacks)

        if valid and value > bestSolutionValue:
            bestSolutionValue = value
            bestSolution = solution
            bestSolutionValid = True
    
    if not bestSolutionValid:
        raise Exception("We found invalid solution...")

    return bestSolutionValue, bestSolution

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
    globalMax = randomSolution(len(weights), len(knapsacks))
    globalMaxValid, globalMaxVal = evaluate(globalMax, values, weights, knapsacks)

    localMax = globalMax
    localMaxVal = globalMaxVal
    localMaxValid = globalMaxValid
    
    while True:
        neighborhood = buildNeighborhood(globalMax, len(knapsacks))

        for solution in neighborhood:
            valid, totalValue = evaluate(solution, values, weights, knapsacks)

            if valid and (totalValue > localMaxVal or not localMaxValid):
                localMaxVal = totalValue
                localMax = solution
                localMaxValid = True

        if localMaxVal > globalMaxVal or localMaxValid and not globalMaxValid:
            globalMaxVal = localMaxVal
            globalMax = localMax
            globalMaxValid = True
        else:
            break
    
    return globalMaxVal, globalMax, globalMaxValid

"""
Creates a random solution that we use as a starting point
"""
def randomSolution(numOfItems, numOfKnap):
    solution = []

    for i in range(numOfItems):
        solution.append(generator.randint(0, numOfKnap))

    return solution
