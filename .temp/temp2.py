from collections import defaultdict
def find_frequency(string):
    count_dict = defaultdict(int)
    for chr in string:
        count_dict[chr] += 1
    return count_dict

print(find_frequency("kolkatta"))
