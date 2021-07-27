# Find number of g in "get going"

def count_letter_in_string(string, search_chr):
    count = 0
    for chr in string:
        if chr == search_chr:
            count += 1
    return count

print(count_letter_in_string("get going", "g"))
# 3
