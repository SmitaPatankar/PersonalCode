"""
Output the count of words in file
"""

from collections import defaultdict

with open("C:/SMITA PERSONAL REPOSITORY/GITHUB CODE/_puzzles/count_each_word_from_text_file.py", "r") as f:
    lines = f.readlines()

word_count = defaultdict(int)
excluded_character_combinations = [".\n", ",", "."]

for line in lines:
    temp = line.split(" ")
    for i in range(len(temp)):
        word = temp[i]
        for chr in excluded_character_combinations:
            if word.endswith(chr):
                word = word[:len(word)-len(chr)]
                break
        word_count[word] += 1

print(dict(word_count))
