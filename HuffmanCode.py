import csv


def huffman(file):
    with open(file, 'r') as data:
        reader = csv.reader(data)
        weightList = {}
        trees = []
        i = 0
        for line in reader:
            if i == 0:
                numNodes = line[0]
                i += 1
                continue
            weightList[tuple([i])] = int(line[0])
            trees.append(tuple([i]))
            i += 1
        # print(trees)
        # print(weightList)
        j = 0
        depth = 0
        depth2 = 0
        while len(trees) >= 2:
            t1 = 0
            t2 = 0
            list1 = sorted(weightList.values())
            # print(list1)
            for key, value in weightList.items():
                if value == list1[0]:
                    t1 = key
                elif value == list1[1]:
                    t2 = key
                elif j == 0 and value == list1[::-1][0]:
                    maxfreq = key
            if j == 0:
                lastnode = t1[0]
                firstnode = maxfreq[0]
            print(t1, ", ,", t2, "/\/", maxfreq)
            trees.remove(t1)
            trees.remove(t2)
            t3 = list(t1) + list(t2)
            if lastnode in t3:
                depth += 1
            if firstnode in t3:
                depth2 += 1
            trees.append(tuple(t3))
            weightList[tuple(t3)] = weightList[t1] + weightList[t2]
            weightList.__delitem__(t1)
            weightList.__delitem__(t2)
            j += 1
        print(len(trees[0]))
        print(depth, depth2, sep='\t')



if __name__ == '__main__':
    huffman('huffman.txt')