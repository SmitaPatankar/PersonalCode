# char array in cpp
"""
- just like int array but with char data type
- first empty block has null character as terminator to denote that string has ended there
- null's ascii value is 0
- if we add null manually in between, processing will stop there itself
- can be input at once
- null character is typed as \o
"""

# string in cpp
"""
1d char array
"""

# program: cpp: length of string
"""
count till null character
"""

# program: https://leetcode.com/problems/reverse-string/
# logic: keep start and end, swap and move closer, stop when s>= e
"""
def reverse_string(s):
    start = 0
    end = len(s) - 1
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    return "".join(s)
print(reverse_string(["s","m","i"]))
"""

# hw: program: https://www.codingninjas.com/codestudio/problems/check-if-the-string-is-a-palindrome_1062633
# ignore sumbols and spaces, consider alphabets and numbers only
# string is not case sensitive
# logic: keep start and end, compare, move closer, stop when s>=e or mismatch found
# logic: for case insensitive:
# check lower as ord lies between that of a and z
# convert to uppe as see how far ord of big character is from that of big A
# return character with ord as ord of big A + above diff
# similarly for string "9" to int 1
# check diff from "0" to "9" ord
# add that to 0
# logic for alphanum - check if ord is in range of A,Z,a,z,0,9
"""
def is_alpha_num(c):
    if ord("a") <= ord(c) <= ord("z") or ord("A") <= ord(c) <= ord("Z") or ord("0") <= ord(c) <= ord("9"):
        return True
    return False
def lower_char(c):
    if ord("a") <= ord(c) <= ord("z") or ord("0") <= ord(c) <= ord("9"):
        return c
    else:
        diff = ord(c) - ord("A")
        lower_ord = ord("a") + diff
        return chr(lower_ord)
def check_palindrome(s):
    start = 0
    end = len(s) - 1
    while start < end:
        if not is_alpha_num(s[start]):
            start += 1
        elif not is_alpha_num(s[end]):
            end -= 1
        else:
            if lower_char(s[start]) != lower_char(s[end]):
                return False
            else:
                start += 1
                end -= 1
    return True
print(check_palindrome("c1 O$d@eeD o1c"))  # true
print(check_palindrome("N2 i&nJA?a& jnI2n"))  # true
print(check_palindrome("A1b22Ba"))  # false
print(check_palindrome("codingninjassajNiNgNidoc"))  # true
print(check_palindrome("5?36@6?35"))  # true
print(check_palindrome("aaBBa@"))  # false
print(check_palindrome(" "))  # true
"""

# program: https://leetcode.com/problems/valid-palindrome/
# same as above

# hw: program: https://leetcode.com/problems/reverse-words-in-a-string-ii/
# program: reverse sequence of words in string
# logic: first reverse letters of each word, then reverse entire string
# logic for reverse letters of each word: mark start and end at 0 and move end forward till space is found, reverse that portion, move start and end ahead of space, process last word outside loop as there is no space after that
"""
def reverse(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
def reverse_letters_of_words(s):
    start = 0
    end = 0
    while end <= len(s) - 1:
        if s[end].isspace():
            reverse(s, start, end-1)
            start = end + 1
            end += 1
        else:
            end += 1
    reverse(s, start, end - 1)
def reverse_words_in_string(s):
    reverse_letters_of_words(s)
    print(s)
    reverse(s, 0, len(s)-1)
s = list("my name is smita")
print(s)
reverse_words_in_string(s)
print(s)  # smita is name my
"""

# program: https://practice.geeksforgeeks.org/problems/maximum-occuring-character-1587115620/1
# logic make array for a-z and A-Z and keep count there
# use ascii conversions for number to letter and back
# lower case only
# time O(n) # space constant
"""
def get_max_occurring_character(s):
    a = [0]*52  # for a-z and A-Z
    for i in range(len(s)):
        if ord("a") <= ord(s[i]) <= ord("z"):
            index = ord(s[i]) - ord("a")
        else:
            index = ord(s[i]) - ord("A") + 26
        a[index] = a[index] + 1 if a[index] else 1
    max_index = -1
    max_value = -1
    for i in range(len(a)):
        if a[i] > max_value:
            max_value = a[i]
            max_index = i
    if 0 <= max_index <= 25:
        max_index = max_index + ord("a")
    else:
        max_index = max_index + ord("A") - 26
    return chr(max_index)
print(get_max_occurring_character("smitapatttttankar"))
"""

# program: https://www.codingninjas.com/codestudio/problems/replace-spaces_1172172
# logic: new string
# O(n) time and space
"""
def replace_spaces(s):
    ans = ""
    for i in range(len(s)):
        if s[i] != " ":
            ans += s[i]
        else:
            ans += "@40"
    return ans
s = "smita vijay patankar"
print(s)
print(replace_spaces(s))
"""

# hw: program: https://www.codingninjas.com/codestudio/problems/replace-spaces_1172172
# in place
# logic count spaces
# count extra length needed to replace spaces with new character(s)
# expand string by that many spaces
# start filling from reverse
"""
def replace_spaces(s):
    # space count
    space_count = 0
    for c in s:
        if c == " ":
            space_count += 1
    # extra space needed to accomodate "@40" in place of " "
    original_length = len(s)
    extra_length_needed = space_count * 2
    new_length = original_length + extra_length_needed
    # extend string with extra length
    for i in range(extra_length_needed):
        s += " "
    # last indexes of extended string to fill from backwards along with "@40" in place of " "
    new_index_from_back = new_length - 1
    # fill from backwards along with "@40" instead of " "
    s = list(s)
    for original_index_from_back in range(original_length - 1, -1, -1):
        if s[original_index_from_back] == " ":
            s[new_index_from_back] = "0"
            s[new_index_from_back-1] = "4"
            s[new_index_from_back-2] = "@"
            new_index_from_back -= 3
        else:
            s[new_index_from_back] = s[original_index_from_back]
            new_index_from_back -= 1
    return "".join(s)
s = "smita vijay patankar"
print(s)
print(replace_spaces(s))
"""

# todo: python: check how find and replace works internally
# program: https://leetcode.com/problems/remove-all-occurrences-of-a-substring/
# one at a time
# logic: loop while part exists, replace it with blank
"""
def remove_substring(s, part):
    while s.find(part) != -1:
        s = s.replace(part, "", 1)
    return s
s = "daabcbaabcbc"
part = "abc"
print(remove_substring(s, part))
"""

# program: https://leetcode.com/problems/permutation-in-string/
# check if s1's permutation is present in s2
# keep count of characters in s1
# on s2, travel in window of s1 length
# keep count in another array and compare
# else move forward and minus left element and + right element
# O(m+n) time and constant space
"""
def check_permutation_present(s1, s2):
    # convert strings to char arrays
    s1 = list(s1)
    s2 = list(s2)
    # create array for saving their character counts
    s1_count = [0]*26
    s2_count = [0]*26
    # save s1 char count
    for i in range(len(s1)):
        index = ord(s1[i]) - ord("a")
        s1_count[index] += 1
    # check first window on s2 for match
    i = 0
    window_size = len(s1)
    while i < window_size and i < len(s2):
        index = ord(s2[i]) - ord("a")
        s2_count[index] += 1
        i += 1
    if s1_count == s2_count:
        return True
    # check further windows on s2 till end or match
    while i < len(s2):
        removed_char_index = ord(s2[i-window_size]) - ord("a")
        added_char_index = ord(s2[i]) - ord("a")
        s2_count[removed_char_index] -= 1
        s2_count[added_char_index] += 1
        if s1_count == s2_count:
            return True
        i += 1
    return False
s1 = "tim"
s2 = "smita"
print(check_permutation_present(s1, s2))
"""

# hw: program: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
# logic: keep each element in new array and if same element is found next, pop that from collected array
"""
def remove_adjacent_duplicates(s):
    previous_elements = []
    for element in s:
        if previous_elements and previous_elements[-1] == element:
            previous_elements.pop()
        else:
            previous_elements.append(element)
    return "".join(previous_elements)
s = ("azxxzy")
print(remove_adjacent_duplicates(s))
"""

# todo: revise
# program: https://leetcode.com/problems/string-compression/
# [a,a,b,c,c,c]
# [a,2,b,c,3]
# for single character just give character
# no extra space
# return size of new array
# logic
# outer loop till we traverse complete array
# inner loop
# start, end=next
# compare and keep looping
# break when not matched or end of array if matched move forward
# when matched
# store in original array and keep track of length of that array
# constant space, linear time
"""
def compress_string(s):
    start = 0
    ansindex=0
    n = len(s)
    while start < n:
        end = start + 1
        while end < n and s[end] == s[start]:
            end += 1
        # different character or end reached
        s[ansindex] = s[start]
        ansindex += 1
        count = end - start
        if count > 1:
            count = str(count)
            for character in count:
                s[ansindex] = character
                ansindex += 1
        start = end
        end += 1
    print(s)
    print(ansindex)
s = ['a','a','b','c','c','c']
print(compress_string(s))
"""
