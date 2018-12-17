from random import Random
import numpy as np

seed = 4523
generator = Random(seed)

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

def buildNeighborhood(solution, numOfKnap):
    numOfSolutions = len(solution)
    solutions = []

    for i in range(numOfSolutions):
        solutions.append(solution[:])
        if solutions[i][i] >= numOfKnap:
            solutions[i][i] = 0
        else:
            solutions[i][i] += 1

    return solutions

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

def neighborhoodSearchIteration(weights, values, knapsacks):
    globalMax = randomSolution(len(weights), len(knapsacks))
    globalMaxValid, globalMaxVal = evaluate(globalMax, values, weights, knapsacks)

    localMax = globalMax
    localMaxVal = globalMaxVal
    localMaxValid = globalMaxValid
    
    for _ in range(100):
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

def randomSolution(numOfItems, numOfKnap):
    solution = []

    for i in range(numOfItems):
        solution.append(generator.randint(0, numOfKnap))

    return solution
