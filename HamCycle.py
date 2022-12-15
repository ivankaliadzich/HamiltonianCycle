import itertools
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


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


            # Function to draw a graph using library matplotlib.pyplot
def add_edge(f_item, s_item, graph=None):
    graph.add_edge(f_item, s_item)
    graph.add_edge(s_item, f_item)


            # Inputing number of vertices and edges, making a matrix of graph adjancy (graph is undirected)
print("Input number of vertices:")
n = int(input())
print("Input number of edges:")
m = int(input())

graph = nx.Graph()
graph.nodes()

matrix = []
for i in range(n):
    matrix.append([0]*n)

print("Write what vertices you want to connect \n(counting start from 0 and graph is undirected)")
for i in range(m):
    x,y = input().split()
    x = int(x)
    y = int(y)
    matrix[x][y]=1
    matrix[y][x]=1
    add_edge(x, y, graph=graph)

mustBe = []
CycleAns = []


            # Adding obligatory edges
print("Write how many edges are obligatory in Hamiltonian Cycle:")
e = int(input())
if e != 0:
    print("Write what vertices must be connected in Hamiltonian Cycle:")
    for i in range(e):
        x, y = input().split()
        x = int(x)
        y = int(y)
        mustBe.append([x, y])

FindPossibleCycle(matrix)

print("\nAll possible Hamiltonian Cycles:")
if len(allHamCycle) == 0:
    print("No Hamiltonian Cycle in graph")
else:
    for i in range(len(allHamCycle)):
        print(i+1, end="")
        print(")", end=" ")
        for j in range(len(allHamCycle[i])):
            if j != len(allHamCycle[i])-1:
                print(allHamCycle[i][j], end=" -> ")
            else:
                print(allHamCycle[i][j])


            # Outputing answer with drawing graph using library matplotlib.pyplot
nx.draw_circular(graph, node_color = 'green', node_size=1000, with_labels=True)
print("\nHamiltonian Cycles with obligatory edges:")

if e != 0:
    OK = False
    for i in range(len(allHamCycle)):
        for j in range(len(mustBe)):
            OK = False
            for q in range(len(allHamCycle[i]) - 1):
                if ((allHamCycle[i][q] == mustBe[j][0] and allHamCycle[i][1 + q] == mustBe[j][1])
                        or (allHamCycle[i][q] == mustBe[j][1] and allHamCycle[i][1 + q] == mustBe[j][0])):
                    OK = True
                    break
            if OK == False:
                break
        if OK == True:
            CycleAns.append(allHamCycle[i])
else:
    CycleAns = allHamCycle

if len(CycleAns) == 0:
    print("There is no Hamiltonian Cycles with your obligatory edges")
else:
    for i in range(len(CycleAns)):
        print(i + 1, end="")
        print(")", end=" ")
        for j in range(len(CycleAns[i])):
            if j!=len(CycleAns[i])-1:
                print(CycleAns[i][j], end=" -> ")
            else:
                print(CycleAns[i][j])

plt.show()
