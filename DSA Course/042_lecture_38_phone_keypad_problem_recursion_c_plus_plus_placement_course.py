# program - https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# string contains digits from 2 to 9
# return all possible letter combinations in any order
# 2 = abc
# 3 = def
# 4 = ghi
# 5 = jkl
# 6 = mno
# 7 = pqrs
# 8 = tuv
# 9 = wxyz
# eg:
# 23
# ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# backtracking removal of added letter to current is done in cpp because string is mutable so we need to make it blank again before next letter's processing
"""
def solve(letter_combos, index, current, ans):
    if index >= len(letter_combos):
        if current:
            ans.append(current)
        return
    for j in range(len(letter_combos[index])):
        current = current + letter_combos[index][j]
        solve(letter_combos, index+1, current, ans)
        current = current.replace(letter_combos[index][j], "")
def letter_combinations(digits):
    index = 0
    current = ""
    ans = []
    digit_to_letters = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    letter_combos = [digit_to_letters[int(digit)] for digit in digits]
    solve(letter_combos=letter_combos, index=index, current=current, ans=ans)
    return ans
digits = "23"
print(letter_combinations(digits))
"""
