import csv


def read_path(file):
    with open(file, 'r') as data:
        reader = csv.reader(data)
        weightlist = {}
        i = 0
        for line in reader:
            if i == 0:
                numpoints = line[0]
                i += 1
                continue
            weightlist[i] = int(line[0])
            i += 1
        print(weightlist)
        return weightlist


def wis(data):
    weighttrack = {0: 0, 1: data[1]}
    for i in range(2, len(data)+1):
        weighttrack[i] = max(weighttrack[i-1], weighttrack[i-2] + data[i])
    print(weighttrack)
    return weighttrack


def wis_reconstruct(weights, wisdata):
    current = []
    i = len(weights)
    while i >= 2:
        if wisdata[i-1] >= wisdata[i-2] + weights[i]:
            i -= 1
        else:
            current.append(i)
            i -= 2
    if i == 1:
        current.append(i)
    return current




if __name__ == '__main__':
    weightlist = read_path('mwis.txt')
    wis_found = wis(weightlist)
    wis_list = wis_reconstruct(weightlist, wis_found)
    print(wis_list)
    checkset = {1, 2, 3, 4, 17, 117, 517, 997}
    found = {x: '0' for x in checkset}
    print(wis_found[len(weightlist)])
    for i in wis_list:
        if i in checkset:
            found[i] = '1'
    print(found)
    result = [val for val in found.values()]
    print(str(result))
    # print(wis_found)
    # print(wis_list)