# program: permutations - https://www.codingninjas.com/codestudio/problems/permutations-of-a-string_985254
# array of unique integers
# return all possible permutations in any order
# eg: [1,2,3]
# ans: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
def solve(str, index, ans):
    print(f"f({str}, {index}, {ans})")
    if index >= len(str):
        print(f"appending {str} to {ans}")
        ans.append(str.copy())
        return
    for i in range(index, len(str)):
        if i != index:
            str[index], str[i] = str[i], str[index]
        solve(str, index+1, ans)
        if i != index:
            str[index], str[i] = str[i], str[index]
def generate_permutations(str):
    str = [c for c in str]
    index = 0
    ans = []
    solve(str, index, ans)
    return ["".join(str) for str in ans]
str = "abc"
print(generate_permutations(str))
"""

# hw: permutations of string by checking which space is filled and which is empty - high space complexity
"""
def solve(str, index, output, ans):
    print(f"f({''.join(str)}, {index}, {''.join(output)}, {[''.join(x) for x in ans]})")
    if index >= len(str):
        print(f"appending {''.join(output)} to {[''.join(x) for x in ans]}")
        ans.append(output.copy())
        return
    for i in range(len(str)):
        if str[i] not in output:
            output.append(str[i])
            solve(str, index+1, output, ans)
            output.remove(str[i])
def generate_permutations(str):
    str = [c for c in str]
    index = 0
    output = []
    ans = []
    solve(str, index, output, ans)
    return ["".join(str) for str in ans]
str = "abc"
print(generate_permutations(str))
"""