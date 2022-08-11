import random

def randomSolution(tsp):
    cities = list(range(len(tsp)))
    solution = []

    for i in range(len(tsp)):
        randomCity = cities[random.randint(0, len(cities) - 1)]
        solution.append(randomCity)
        cities.remove(randomCity)

    return solution

def routeDist(tsp, solution):
    routeDist = 0
    for i in range(len(solution)):
        routeDist += tsp[solution[i - 1]][solution[i]]
    return routeDist

def getNeighbours(solution):
    neighbours = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            neighbours.append(neighbour)
    return neighbours

def getBestNeighbour(TravellingSalesmanProblem, neighbours):
    bestRouteDist = routeDist(TravellingSalesmanProblem, neighbours[0])
    bestNeighbour = neighbours[0]
    for neighbour in neighbours:
        currentRouteDist = routeDist(TravellingSalesmanProblem, neighbour)
        if currentRouteDist < bestRouteDist:
            bestRouteDist = currentRouteDist
            bestNeighbour = neighbour
    return bestNeighbour, bestRouteDist

def hillClimbing(TravellingSalesmanProblem):
    currentSolution = randomSolution(TravellingSalesmanProblem)
    currentRouteDist = routeDist(TravellingSalesmanProblem, currentSolution)
    neighbours = getNeighbours(currentSolution)
    bestNeighbour, bestNeighbourRouteDist = getBestNeighbour(TravellingSalesmanProblem, neighbours)

    while bestNeighbourRouteDist < currentRouteDist:
        currentSolution = bestNeighbour
        currentRouteDist = bestNeighbourRouteDist
        neighbours = getNeighbours(currentSolution)
        bestNeighbour, bestNeighbourRouteDist = getBestNeighbour(TravellingSalesmanProblem, neighbours)

    return currentSolution, currentRouteDist

def main():
    TravellingSalesmanProblem = [
        [0, 400, 250, 200],
        [400, 0, 170, 350],
        [250, 170, 0, 700],
        [200, 350, 700, 0]
    ]

    print(hillClimbing(TravellingSalesmanProblem))

if __name__ == "__main__":
    print("Using Hill CLimbing for TSP\n\n Nodes,  Total Cost")
    main()
    
    
