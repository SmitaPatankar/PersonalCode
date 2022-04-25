# time complexity details
"""
- time taken by an algorithm to run as a function of length of the input
- determines whether a program/algorithm is good or bad
- helps write better programs and compare different programs
- cant comapre algorithms based on runtime because runtime depends on whether machine on which it is run is slow or fast
- notations - BigO, Theta, Omega
    - BigO - upperbound i.e. worst case
    - theta - average i.e. average case
    - omega - lower bound i.e. best case
- different time complexities in descending order:
    - constant - O(1) - eg: no variable
    - logarithmic - O(logn) - eg: binary search
    - linear - O(n) - eg: runs as many times as variable number
    - O(n log n)
    - quadratic - O(n^2) - eg: 2 nested loops
    - cubic - O(n^3) - eg: 3 nested loops
    - O(2^n)
    - O(n!)
- how to calculate
    - ignore constants
    - ignore lower degree
    - when loops are separate, add their complexities
    - when loops are nested, multiply their complexities
- examples
    - loop - O(n)
    - reverse array - O(n)
    - linear search - O(n)
    - min/max - O(n)
    - isprime - O(n)
    - counting - O(n)
- time limit exceeded
    - modern machines execute 10^8 operations per second
    - read constraints from programming question to figure which algorithm is suitable
- max complexities chart
    - 10^8 - O(1),O(logn), O(n)
    - 10^6 - O(n log n)
    - 10^4 - O(n^2)
    - 2000 - O(n^2 log n)
    - 400 - O(n^3)
    - 100 - O(n^4)
    - 15 to 18 - O(2^n n^2)
    - 10 to 11 - O(n!), O(n^6)
"""

# space complexity details
"""
- memory taken by algorithm as a function of the length of input
- examples
    - variables - O(1)
    - fixed size array - O(1)
    - variable size array - O(n)
    - variable size array getting created again and again in loop from scratch - O(n)
"""