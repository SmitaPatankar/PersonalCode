"""
Input:
"smita patankar"

Ouput:
A = 4
"""

def count_letter(string, letter):
    count = 0
    for element in string:
        if element == letter:
            count += 1
    return f"{letter} = {count}"
