# Convert a Number to Words (123 to Hundred Twenty Three)

# 9 - nine
# 99 - ninety nine
# 999 - nine hundred and nine
# 9999 - nine thousand and ninety nine

def num_to_word(n):
    n = str(n)
    string = ""
    singles = ["zero", "one", "two", "three",
                     "four", "five", "six", "seven",
                     "eight", "nine"]
    doubles = ["ten", "eleven", "twelve",
                  "thirteen", "fourteen", "fifteen",
                  "sixteen", "seventeen", "eighteen",
                  "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    tens_power = ["", "", "hundred", "thousand"]
    for i in range(0, len(n)):
        digit = int(n[i])
        pos = len(n) - i
        print(f"digit {digit} position {pos}")
        if pos in [3,2]:
            string += singles[digit]
            string += tens_power[pos]
        elif pos == 1:
            string += tens[digit]
        elif pos == 0:
            string += singles[digit]
        print(string)
    return string

print(num_to_word(999))
