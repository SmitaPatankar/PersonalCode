# find anagram
# checking off
# quadratic
"""
def are_anagrams(s1, s2):
    anagram = True
    if len(s1) != len(s2):
        anagram = False
    s2_list = list(s2)
    pos_s1 = 0
    while pos_s1 < len(s1) and anagram:
        pos_s2 = 0
        found = False
        while pos_s2 < len(s2_list) and not found:
            if s2_list[pos_s2] == s1[pos_s1]:
                found = True
            else:
                pos_s2 += 1
        if found:
            s2_list[pos_s2] = None
        else:
            anagram = False
        pos_s1 += 1
    return anagram
print(are_anagrams("python", "typhon"))
print(are_anagrams("python", "typlon"))
"""

# find anagram
# sort and compare
# quadratic or linear log
"""
def are_anagrams(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)
    pos = 0
    anagram = True
    while pos < len(s1) and anagram:
        if s1[pos] == s2[pos]:
            pos += 1
        else:
            anagram = False
    return anagram
print(are_anagrams("python", "typhon"))
print(are_anagrams("python", "typlon"))
"""

# find anagram
# brute force
# make all possible strings from s1 and then see if s2 is present in them
# n!

# find anagram
# count and compare
# linear
"""
def are_anagrams(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26
    for c in s1:
        pos = ord(c) - ord("a")
        c1[pos] += 1
    for c in s2:
        pos = ord(c) - ord("a")
        c2[pos] += 1
    i = 0
    anagram = True
    while i < 26 and anagram:
        if c1[i] == c2[i]:
            i += 1
        else:
            anagram = False        
    return anagram
print(are_anagrams("python", "typhon"))
print(are_anagrams("python", "typlon"))
"""
