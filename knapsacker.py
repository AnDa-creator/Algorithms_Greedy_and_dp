import csv
import sys
sys.setrecursionlimit(10**6)
output = {}
def read_data(file):
    with open(file, 'r') as data:
        print("reading data...")
        reader = csv.reader(data, delimiter=' ')
        knap_profile = {}
        i = 0
        for line in reader:
            if i == 0:
                num_points = int(line[1])
                total_weight = int(line[0])
            else:
                knap_profile[i] = {"value": int(line[0]), "weight": int(line[1])}
            i += 1

    # print(knap_profile)
    print("Data reading done")
    return num_points, total_weight,knap_profile


def knapsackered_small(data):
    num_points = data[0]
    total_weight = data[1]
    knap_profile = data[2]
    # Array Initialization
    output = []
    for i in range(0, num_points + 1):
        output.append([])
        for j in range(0, total_weight + 1):
            output[i].append(0)
    # print(output)
    i = 0
    j = 0
    for i in range(1, num_points + 1):
        for j in range(0, total_weight + 1):
            # print(i)
            if knap_profile[i]['weight'] > j:
                output[i][j] = output[i-1][j]
            else:
                output[i][j] = \
                    max(output[i-1][j], output[i-1][j - knap_profile[i]['weight']] + knap_profile[i]['value'])
    print(output[num_points][total_weight])


def knapsackered_big(data):
    num_points = data[0]
    total_weight = data[1]
    knap_profile = data[2]
    # if num_points % 10 == 0:
    #     print("At point for {}".format(num_points))
    # print(num_points)
    # print(val)
    # print(new_profile)
    if num_points == 0 or total_weight == 0:
        return 0
    if (num_points,total_weight) in output.keys():
        # print("returned earlier")
        return output[(num_points,total_weight)]
    val = knap_profile[num_points]['value']
    weight = knap_profile[num_points]['weight']
    data_second = (num_points - 1, total_weight, knap_profile)
    maxvalue2 = knapsackered_big(data_second)
    if total_weight - weight < 0:
        output[(num_points,total_weight)] = maxvalue2
        return output[(num_points,total_weight)]
    else:
        data_first = (num_points - 1, total_weight - weight, knap_profile)
        maxvalue1 = knapsackered_big(data_first)
        output[(num_points,total_weight)] = max(maxvalue2, val + maxvalue1)
        return output[(num_points,total_weight)]

    # print(maxvalue1, maxvalue2, "hi")
    # print(maxvalue1, maxvalue2)
    # return max(maxvalue2, maxvalue1)


if __name__ == '__main__':
    data = read_data('knapsack_big.txt')
    # knapsackered_small(data)
    print('hello')
    max_sack = knapsackered_big(data)
    print(max_sack)
