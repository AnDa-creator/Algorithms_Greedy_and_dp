import csv


def read_graph(file):
    with open(file, 'r') as data:
        reader = csv.reader(data, delimiter= ' ')
        print("Reading Data...")
        i = 0
        points = []
        for line in reader:
            if i == 0:
                numnodes = int(line[0])
                numbits = int(line[1])
                print(numbits)
                i += 1
                continue
            newpoint = ''
            for index in range(0, numbits):
                newpoint += line[index]
            points.append(int(newpoint, 2))
            i += 1
        print("Data read successfully")
        # print(numnodes, numbits, points)
        return numnodes, numbits, points


# def similarity(point1, point2):
#     pass
#     return creds

def  countSetBits(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count


def sort_vector(data, maxspace):
    points = sorted(list(set(data[2])))
    setDict = {}
    clusters = {}
    for num in points:
        countnow =  countSetBits(num)
        setDict[num] = countnow
        clusters[num] = num
    # print(setDict)
    numClusters = len(points)
    points_copy = [x for x in points]
    for num in points_copy:
        for num2 in points_copy:
            if abs(setDict[num] - setDict[num2]) < maxspace and clusters[num] != clusters[num2]:
                check = num^num2
                if countSetBits(check) in range(1, maxspace):
                    if num < num2:
                        temp = clusters[num2]
                        for val in clusters.keys():
                            if clusters[val] == temp:
                                clusters[val] = clusters[num]
                    else:
                        temp = clusters[num]
                        for val in clusters.keys():
                            if clusters[val] == temp:
                                clusters[val] = clusters[num2]
                    numClusters -= 1
                    if numClusters % 1000 == 0:
                        print("Number of clusters now is {}".format(numClusters))
                        # print("hi2", num)
    print(numClusters)
    # print(clusters)



# def findclustering(data, maxspace):
#     ordered_dict = {k: v for k, v in sorted(data[2].items(), key=lambda item: item[1])}
#     print(len(ordered_dict))
#     numcluster = 0
#     for vertex in range(1, data[0] + 1):
#         numcluster += 1
#     temp = numcluster
#     print(temp)
#     calculated = []
#     temp2 = 0
#     for item in ordered_dict.keys():
#         for item2 in ordered_dict.keys():
#             if abs(ordered_dict[item2]- ordered_dict[item]) < maxspace and item != item2:
#                 nowcase = (item, item2)
#                 nowcase2 = (item2, item)
#                 if nowcase not in calculated and nowcase2 not in calculated:
#                     if similarity(item, item2) <= 2:
#                         # print(item, item2, "similarity is ", similarity(item, item2))
#                         numcluster -= 1
#                     calculated.append(nowcase)
#                     calculated.append(nowcase2)
#                 if abs(temp - numcluster) % 100 == 0 and temp2 != numcluster:
#                     print("currently number of clusters is: {} and items were {}, {}".format(numcluster, nowcase, nowcase2))
#                     temp2 = numcluster
#             elif item2 == item:
#                 continue
#             else:
#                 break

    # print(numcluster)




if __name__ == '__main__':
    data = read_graph('clustering_big.txt')
    # findclustering(data, 3)
    sort_vector(data, 3)