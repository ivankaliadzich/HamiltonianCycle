import itertools
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import random
from networkx.generators.random_graphs import erdos_renyi_graph
import time

start = time.time()

n = 10


allHamCycle = []
            # Function to check if a vertex can be added at index pos in the Hamiltonian Cycle
def CheckingVetrexToCycle(vertex, matrix, path, index):
    if matrix[path[index-1]][vertex] == 0:
        return False
    for i in range(index):
        if path[i] == vertex:
            return False
    return True

hasCycle = False


            # Function to find all possible Hamiltonian Cycles
def FindPossibleCycle(matrix):
    global hasCycle
    hasCycle = False
    path = []
    path.append(0)
    visited = [False] * (len(matrix))
    for i in range(len(visited)):
        visited[i] = False
    visited[0] = True
    FindHamiltonCycles(matrix, 1, path, visited)
    if hasCycle == True:
        print("No Hamiltonian Cycle")
        return


            # Recursive function to find all Hamiltonian Cycles
def FindHamiltonCycles(matrix, index, path, visited):
    if index == len(matrix):
        if matrix[path[-1]][path[0]]!=0:
            path.append(0)
            oneCycle = []
            for i in range(len(path)):
                oneCycle.append(path[i])
            allHamCycle.append(oneCycle)

            path.pop()
            hasCycle = True
        return
    for v in range(len(matrix)):
        if CheckingVetrexToCycle(v, matrix, path, index) and visited[v] == False:
            path.append(v)
            visited[v] = True
            FindHamiltonCycles(matrix, index+1, path, visited)
            visited[v] = False
            path.pop()


def add_edge(f_item, s_item, graph=None):
    graph.add_edge(f_item, s_item)
    graph.add_edge(s_item, f_item)


graph = nx.Graph()
graph.nodes()



matrix = np.random.randint(0,2,(n,n))
for i in range(n):
    for j in range(n):
        if i <= j:
            matrix[i][j] = 0
        else:
            if matrix[i][j] == 1:
                matrix[j][i]=1

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1 :
            add_edge(i, j, graph=graph)



FindPossibleCycle(matrix)

nx.draw_circular(graph, node_color = 'green', node_size=1000, with_labels=True)

#print(allHamCycle)

end = time.time() - start
print("\n", end)

plt.show()
