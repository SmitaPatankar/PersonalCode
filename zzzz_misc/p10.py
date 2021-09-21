# print duplicate characters
# or
# give count of given character

s = "Khushboo"
from collections import defaultdict
d = defaultdict(int)
for character in s:
    d[character] += 1
for k, v in d.items():
    if v > 1:
        print(f"{k} occurs more than once")

# #############################################

character_to_count = "h"
s = "Khushboo"
count = 0
for character in s:
    if character == character_to_count:
        count += 1
print(f"{character_to_count} occurs {count} times")
