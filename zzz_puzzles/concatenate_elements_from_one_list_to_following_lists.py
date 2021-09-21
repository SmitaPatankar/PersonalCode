"""
Input:
[['a','b'],['c','d']]
[['a','b','c'],['d','e','f'],['g','h','i']]

Output:
Ac
Ad
Bc
Bd
"""

all_lists = [['a','b'],['c','d']]
for i in range(len(all_lists)):
    for j in range(i+1, len(all_lists)):
        for element1 in all_lists[i]:
            for element2 in all_lists[j]:
                print(element1+element2)
