import csv
from heapq import *

def read_graph(file):
    with open(file, 'r') as graph:
        print('Reading Graph...')
        reader = csv.reader(graph, delimiter=' ')
        i = 0
        verticesList = []
        adjacencyList = []
        for line in reader:
            if i == 0:
                numNodes = int(line[0])
                numEdges = int(line[1])
                verticesList = [i for i in range(1, numNodes+1)]
                for i in range(0, numNodes+1):
                    adjacencyList.append([])
            else:
                adjacencyList[int(line[0])].append((int(line[1]), (int(line[2]))))
                adjacencyList[int(line[1])].append((int(line[0]), int(line[2])))

            i += 1

        # print(adjacencyList)
        print("Graph Creation completed successfully")
        # print(verticesList)
    return verticesList, adjacencyList


def primHeap(graph):
    explored = [1]
    verticesList, adjacencyList = graph[0], graph[1]
    Heap = []
    Tree = []
    keys = {}
    winner = {}
    for vertex in verticesList :
        if vertex == 1:
            continue
        found = False
        for item in adjacencyList[1]:
            if vertex == item[0]:
                keys[vertex] = item[1]
                winner[vertex] = (1, vertex)
                found = True
        if not found:
            keys[vertex] = float('inf')
            winner[vertex] = None
        heappush(Heap, keys[vertex])
    # print(keys)
    # print(winner)
    while len(Heap) != 0:
        min = heappop(Heap)
        for key, value in keys.items():
            if min == value and key not in explored:
                w_star = key
        explored.append(w_star)
        Tree.append(winner[w_star])
        for item in adjacencyList[w_star]:
            if item[0] not in explored:
                point = item[0]
                if item[1] < keys[point]:
                    # print(point, " // " , item[1])

                    Heap.remove(keys[point])
                    heapify(Heap)
                    # print(Heap)
                    keys[point] = item[1]
                    winner[point] = (w_star, point)
                    heappush(Heap, keys[point])
    costlist = []
    for item in Tree:
        for val in adjacencyList[item[0]]:
            if val[0] == item[1]:
                costlist.append(val[1])
    print(sum(costlist))
    # print(costlist)
    print(Tree)

    return Tree


if __name__ == '__main__':
    graph = read_graph("MnimumSpanning.txt")
    primHeap(graph)



