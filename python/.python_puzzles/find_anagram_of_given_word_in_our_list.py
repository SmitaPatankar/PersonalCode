"""
Find the anagram word in the following array: -
Arr = [“depth”, “head”, “earth”, “water”],
Input = heart
Out - earth

Eg :- Def anagram (arr, word):

# efficient
# own logic
# less complexity
"""

lst = ["depth", "head", "earth", "water"]

from collections import defaultdict

def find_anagram(word):
    main_character_count = defaultdict(int)
    for character in word:
        main_character_count[character] += 1
    for element in lst:
        if len(word) != len(element):
            continue
        temp = defaultdict(int)
        for character in element:
            temp[character] += 1
        if temp == main_character_count:
            return element

print(find_anagram("heart"))
# earth
