import csv


def read_data(file):
    with open(file, 'r') as data:
        reader = csv.reader(data, delimiter=' ')
        job_profile = {}
        i = 0
        for line in reader:
            if i == 0:
                num_jobs = int(line[0])
            else:
                job_profile[i] = (int(line[0]), int(line[1]))
            i += 1
    return job_profile, num_jobs


def greedy_diff(data):
    num_jobs = data[1]
    job_profile = data[0]
    difference_set = {}
    for i in range(1, num_jobs+1):
        difference_set[i] = job_profile[i][0] - job_profile[i][1]
    ordered_dict = {k: v for k, v in sorted(difference_set.items(), key=lambda item: item[1], reverse=True)}
    # print(ordered_dict)
    new_profile = {}
    i = 1
    for x in ordered_dict.keys():
        new_profile[i] = (job_profile[x][0], job_profile[x][1], ordered_dict[x])
        i += 1
    # print(new_profile)
    for val in new_profile.keys():
        for val2 in new_profile.keys():
            if new_profile[val][2] == new_profile[val2][2] and new_profile[val][0] > new_profile[val2][0] and val > val2 :
                temp = new_profile[val]
                new_profile[val] = new_profile[val2]
                new_profile[val2] = temp
    # print(new_profile)
    completion = []
    weighted = []
    for item in new_profile.keys():
        weight = new_profile[item][0]
        if len(completion) != 0:
            completionNow = completion[::-1][0] + new_profile[item][1]
        else:
            completionNow = new_profile[item][1]
        # print(weight," // ", completionNow)
        weighted_completion = weight*completionNow
        completion.append(completionNow)
        weighted.append(weighted_completion)
    print(sum(weighted))


def greedy_ratio(data):
    num_jobs = data[1]
    job_profile = data[0]
    ratio_set = {}
    for i in range(1, num_jobs+1):
        ratio_set[i] = job_profile[i][0] / job_profile[i][1]
    ordered_dict = {k: v for k, v in sorted(ratio_set.items(), key=lambda item: item[1], reverse=True)}
    # print(ordered_dict)
    new_profile = {}
    i = 1
    for x in ordered_dict.keys():
        new_profile[i] = (job_profile[x][0], job_profile[x][1], ordered_dict[x])
        i += 1
    # print(new_profile)
    completion = []
    weighted = []
    for item in new_profile.keys():
        weight = new_profile[item][0]
        if len(completion) != 0:
            completionNow = completion[::-1][0] + new_profile[item][1]
        else:
            completionNow = new_profile[item][1]
        # print(weight," // ", completionNow)
        weighted_completion = weight*completionNow
        completion.append(completionNow)
        weighted.append(weighted_completion)
    print(sum(weighted))

if __name__ == '__main__':
    data = read_data("jobs.txt")
    greedy_diff(data)
    greedy_ratio(data)