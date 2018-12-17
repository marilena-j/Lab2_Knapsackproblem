from random import Random
import numpy as np

seed = 4523
generator = Random(seed)

def evaluate(solution, values, weights, knapsacks):
    totalValue = 0
    valid = True

    for knapsack in range(len(knapsacks)):

        weight = 0
        for i in range(len(solution)):
            if solution[i] == knapsack + 1:
                totalValue += values[i]
                weight += weights[i]

        if weight > knapsacks[knapsack]:
            valid = False
    
    return valid, totalValue

def buildNeighborhood(solution, numOfKnap):
    numOfSolutions = len(solution)
    solutions = []

    for i in range(numOfSolutions):
        solutions.append(solution[:])
        if solutions[i][i] == numOfKnap:
            solutions[i][i] = 0
        else: 
            solutions[i][i] += 1
        
    return solutions

def neighborhoodSearch(weights, values, knapsacks):
    bestSolutionValue, bestSolution = neighborhoodSearchIteration(weights, values, knapsacks)

    for _ in range(2):
        value, solution = neighborhoodSearchIteration(weights, values, knapsacks)

        if value > bestSolutionValue:
            bestSolutionValue = value
            bestSolution = solution
    
    return bestSolutionValue, bestSolution

def neighborhoodSearchIteration(weights, values, knapsacks):
    globalMax = randomSolution(len(weights), len(knapsacks))
    _, globalMaxVal = evaluate(globalMax, values, weights, knapsacks)

    localMax = globalMax
    localMaxVal = globalMaxVal
    
    for _ in range(100):
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

def randomSolution(numOfItems, numOfKnap):
    solution = []

    for i in range(numOfItems):
        solution.append(generator.randint(0, numOfItems))

    return solution
