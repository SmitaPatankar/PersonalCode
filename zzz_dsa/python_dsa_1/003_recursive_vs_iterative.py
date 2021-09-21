# iterative (has loops)
# cpu cycles for infinite loops
def pow(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i = i + 1
    return power
print(pow(5))

# recursive
# memory for infinite loops
# many calls are pushed and popped which take memory and time
# easy to code
def pow(n):
    if n == 0:
        return 1
    return pow(n-1) * 2
print(pow(5))

# use memorization of previous results to reduce time complexity
