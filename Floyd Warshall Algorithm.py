# Floyd Warshall Algorithm
V = 4
INF = 99999
  
def floydWarshall(graph):
  
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))
  
    for k in range(V):
  
        # pick all vertices as source one by one
        for i in range(V):
  
            # Pick all vertices as destination for the
            # above picked source
            for j in range(V):
  
                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j]
                                 )
    printSolution(dist)
  
  
# A utility function to print the solution
def printSolution(dist):
    print("\nShortest Distance between every pair of Vertices-\n")
    for i in range(V):
        for j in range(V):
            if(dist[i][j] == INF):
                print("INF",end="\t")
            else:
                print(dist[i][j],end="\t")
            if j == V-1:
                print("")
  
  
# Driver program to test the above program
graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0,   1],
         [INF, INF, INF, 0]
         ]
# Print the solution
floydWarshall(graph)