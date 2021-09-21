"""
Input:
"smita patankar"

Ouput:
A (5,8,10,13)
"""

def find_letter_positions(string, letter):
    positions = []
    for i in range(len(string)):
        if string[i] == letter:
            positions.append(str(i+1))
    return f"{letter} ({','.join(positions)})"

print(find_letter_positions("smita patankar", "a"))
