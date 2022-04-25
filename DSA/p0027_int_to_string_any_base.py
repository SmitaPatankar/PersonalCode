def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return to_str(n // base, base) + convert_string[n % base]


res = to_str(1453, 16)
print(res)
print(type(res))
res = to_str(769, 10)
print(res)
print(type(res))
res = to_str(10, 2)
print(res)
print(type(res))

# todo
"""
Write a function that takes a string as a parameter and returns a new string 
that is the reverse of the old string.

Write a function that takes a string as a parameter and returns True if the string is a palindrome, 
False otherwise. Remember that a string is a palindrome if it is spelled the same both forward and backward. 
For example: radar is a palindrome. 
For bonus points palindromes can also be phrases, but you need to remove the spaces and punctuation 
before checking. 
For example: madam i’m adam is a palindrome. Other fun palindromes include:
kayak
aibohphobia
Live not on evil
Reviled did I live, said I, as evil I did deliver
Go hang a salami; I’m a lasagna hog.
Able was I ere I saw Elba
Kanakanak – a town in Alaska
Wassamassaw – a town in South Dakota
"""
