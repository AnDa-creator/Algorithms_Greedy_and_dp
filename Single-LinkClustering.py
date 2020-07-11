import csv

def read_graph(file):
    with open(file, 'r') as data:
        reader = csv.reader(data, delimiter=' ')
        print("Hi, reading data")
        i = 0
        listedges = {}
        for line in reader:
            if i == 0:
                numnodes = int(line[0])
                print(numnodes)
                i += 1
                continue
            listedges[(int(line[0]), int(line[1]))] = int(line[2])
            i += 1
        print("Graph created successfully")
        # print(len(listedges))
        return numnodes, listedges

def doClustering(data, clustertarget):
    numNodes = data[0]
    currentcluster = {}
    numcluster = 0
    for vertex in range(1, numNodes+1):
        currentcluster[vertex] = vertex
        numcluster += 1

    # print(numNodes)
    ordered_dict = {k: v for k, v in sorted(data[1].items(), key=lambda item: item[1])}
    # print(ordered_dict)

    for val in ordered_dict.keys():
        if currentcluster[val[0]] != currentcluster[val[1]]:
            if val[0] < val[1]:
                temp = currentcluster[val[1]]
                # print(val[0], val[1])
                for num in currentcluster.keys():
                    if currentcluster[num] == temp:
                        # print("hi", num)
                        currentcluster[num] = currentcluster[val[0]]
                        # print("hi2", num)
            else:
                temp = currentcluster[val[0]]
                for num in currentcluster.keys():
                    if currentcluster[num] == temp:
                        # print("hi", num)
                        currentcluster[num] = currentcluster[val[0]]
                        # print("hi2", num)
            numcluster -= 1
            # print(numcluster)
            if numcluster == clustertarget:
                break
    check = []
    for val in currentcluster.values():
        if val not in check:
            check.append(val)
    print("Final number of clusters is {}".format(len(check)))
    print(currentcluster)
    maxspace = float('inf')
    clusterdict = {}
    for val in currentcluster.keys():
        if currentcluster[val] not in clusterdict.keys():
            clusterdict[currentcluster[val]] = [val]
        else:
            clusterdict[currentcluster[val]].append(val)
    print(clusterdict)
    for key1 in clusterdict.keys():
        for values1 in clusterdict[key1]:
            for key2 in clusterdict.keys():
                if key1 != key2:
                    for values2 in clusterdict[key2]:
                        if (values1, values2) in data[1].keys():
                            maxspace = min(maxspace, data[1][(values1, values2)])
                        else:
                            maxspace = min(maxspace, data[1][(values2, values1)])
    print(maxspace)


if __name__ == '__main__':
    data = read_graph("Clustering1.txt")
    doClustering(data, 4)


