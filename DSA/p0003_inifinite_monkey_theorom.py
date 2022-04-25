# infinite monkey theorom
# func1 - generate string of given no. of chars including alphabets and space
# func2 - score the generated string by comparing with original string
# func3 - call both these functions repeatedly until exact string is found
# func3 - everytime a better score is found, print the score and the string
"""
import random
def gen_one(strlen):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    res = ""
    for _ in range(strlen):
        res = res + alphabet[random.randrange(27)]
    return res
def score(goal, teststring):
    num_same = 0
    for i in range(len(teststring)):
        if goal[i] == teststring[i]:
            num_same += 1
    return num_same * 100 / len(goal)
def main():
    goal_string = "methinks it is like a weasel"
    best = 0
    new_string = gen_one(28)
    new_score = score(goal_string, new_string)
    while new_score < 100:
        if new_score > best:
            print(new_score, new_string)
            best = new_score
    new_string = gen_one(28)
    new_score = score(goal_string, new_string)
main()
"""

# todo
# func3 - print best string and so far only after every 1000th try
# hill climbing algorithm i.e. keep result only if it is better than previous one
# keep letters that are correct in best string and modify one character
