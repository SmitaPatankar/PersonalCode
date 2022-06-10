# time complexity
"""
solve via expression or recursion depth
"""

# linear search - time complexity
"""
T(n) = O(n)
"""

# factorial - time complexity
"""
T(base_case) = k1
T(one_case) = k2

f(n) = n * f(n-1)
T(n) = k1 + k2 + T(n-1)

T(n) = k + T(n-1)
T(n-1) = k + T(n-2)
T(n-2) = k + T(n-3)
.
.
.
T(1) = k + T(0)
T(0) = k1

cut cut

T(n) = n * k + k1 = kn + k1 = kn as k1 is constant = n as k is constant

time - O(n) - base case constant
"""

# binary search recursion - time complexity
"""
f(n) = k1 + k2 + f(n/2)

f(n) = k + f(n/2)
f(n/2) = k + f(n/4)
f(n/n) = k + f(0)
f(0) = k

cut cut

logn(k) + k = logn

T(n) = O(logn)
"""

# merge sort - time complexity
"""
main array

recursive break in 2 parts

copy into 2 arrays
merge and put into original array

T(n) = b.c. + mid + T(n/2) + T(n/2) + (copy*n) + (merge*n)
T(n) = K1 + k2 + T(n/2) + T(n/2) + (k3*n) + (k4*n)
T(n) = k + 2T(n/2) + n(k5)
T(n) = 2T(n/2) + n(k5)

T(n) = 2T(n/2) + (n*k)
T(n/2) = 2T(n/4) + (n/2 *k) i.e. 2T(n/2) = 4T(n/4) + n*k
T(n/4) = 2T(n/8) + (n/4 *k) i.e. 4T(n/4) = 8T(n/8) + n*k
T(1) = k

T(n) = 2T(n/2) + (n*k)
2T(n/2) = 4T(n/4) + n*k
4T(n/4) = 8T(n/8) + n*k
T(1) = k

cut cut

T(n) = n*k + n*k + n*k+ k

a*n i..e logn * n i.e. n logn
"""

# todo: hw: solve by this approach - difficult
# fibonacci series - time complexity
"""
T(n) = k1 + k2 + T(n-1) + T(n-2) (base case and sum logic)

T(n) = k + T(n-1) + T(n-2) (base case and sum logic)
T(n-1) = k T(n-2) + T(n-3)
T(n-2) = k + T(n-3) + T(n-4)
T(1) = k1
T(0) = k1

cut cut

T(n) = k + T(n-2) + k + T(n-3) + T(n-4)
"""

# fibonacci series - recursion tree - time complexity
"""
levels are equal to number of elements i.e. n
in each level no of nodes gets multiplied by 2 (not exactly but we are assuming)
elements at last level = 2**n-1 i.e. 2^n

logic time = k

time complexity = k*2^n i.e. 2^n i.e. exponential i..e not good
"""

# todo: learn calculation time complexity using theoroms

# space complexity
"""
maximum space required at any instant of time

when ans is accumulated in ans var, complexity adds up
else gets destroyed after each level

solve via recursion depth
"""

# factorial - space complexity
"""
space allocated for each ans in call stack is getting added up i.e. constant for ans * n = n
"""

# binary search - space complexity
"""
logn levels
each level - mid

i.e. constant * logn i.e. logn
"""

# merge sort - space complexity
"""
logn levels
each level sorts n elements using new array and then returns

k space for mid on each level

k(logn) + n
i.e. n
"""

# fibonacci - space complexity
"""
n levels
each level accumulates ans

n*constant space

i.e. n
"""

# todo: hw: time and space complexity of all recursion program questions from previous lectures - factorial - 34

# todo: hw: time and space complexity of all recursion program questions from previous lectures - power of 2 - 34

# todo: hw: time and space complexity of all recursion program questions from previous lectures - reverse counting - 34

# todo: hw: time and space complexity of all recursion program questions from previous lectures - counting - 34

# todo: hw: time and space complexity of all recursion program questions from previous lectures - fib - 34

# todo: hw: time and space complexity of all recursion program questions from previous lectures - check sorted - 34

# todo: hw: time and space complexity of all recursion program questions from previous lectures - kth child in nth generation - 34

# todo: hw: time and space complexity of all recursion program questions from previous lectures - nth gp term - 34

# todo: hw: time and space complexity of all recursion program questions from previous lectures - print series - 34

# todo: hw: time and space complexity of all recursion program questions from previous lectures - subsets - 34

# todo: hw: time and space complexity of all recursion program questions from previous lectures - move disks - 34

# todo: hw: time and space complexity of all recursion program questions from previous lectures - reach home - 35

# todo: hw: time and space complexity of all recursion program questions from previous lectures - fib - 35

# todo: hw: time and space complexity of all recursion program questions from previous lectures - fib for loop - 35

# todo: hw: time and space complexity of all recursion program questions from previous lectures - stair ways - 35

# todo: hw: time and space complexity of all recursion program questions from previous lectures - say digits - 35

# todo: hw: time and space complexity of all recursion program questions from previous lectures - issorted - 36

# todo: hw: time and space complexity of all recursion program questions from previous lectures - sum of array - 36

# todo: hw: time and space complexity of all recursion program questions from previous lectures - linear search - 36

# todo: hw: time and space complexity of all recursion program questions from previous lectures - binary search - 36

# todo: hw: time and space complexity of all recursion program questions from previous lectures - binary - first and last position - 36

# todo: hw: time and space complexity of all recursion program questions from previous lectures - binary - peak in mountain - 36

# todo: hw: time and space complexity of all recursion program questions from previous lectures - binary - aggressive cows - 36

# todo: hw: time and space complexity of all recursion program questions from previous lectures - binary - book allocation - 36

# todo: hw: time and space complexity of all recursion program questions from previous lectures - binary - pivot - 36

# todo: hw: time and space complexity of all recursion program questions from previous lectures - search in rotated sorted array - 36

# todo: hw: time and space complexity of all recursion program questions from previous lectures - binary sqrt - 36

# todo: hw: time and space complexity of all recursion program questions from previous lectures - reverse string - 37

# todo: hw: time and space complexity of all recursion program questions from previous lectures - reverse string with one pointer - 37

# todo: hw: time and space complexity of all recursion program questions from previous lectures - check palindrome - 37

# todo: hw: time and space complexity of all recursion program questions from previous lectures - check palindrome using one pointer - 37

# todo: hw: time and space complexity of all recursion program questions from previous lectures - power - 37

# todo: hw: time and space complexity of all recursion program questions from previous lectures - bubble sort - 37

# todo: hw: time and space complexity of all recursion program questions from previous lectures - selection sort - 37

# todo: hw: time and space complexity of all recursion program questions from previous lectures - insertion sort - 37

# todo: hw: time and space complexity of all recursion program questions from previous lectures - merge sort - 38

# todo: hw: time and space complexity of all recursion program questions from previous lectures - inversion count - 38

# todo: hw: time and space complexity of all recursion program questions from previous lectures - merge sort in place - 38

# todo: hw: time and space complexity of all recursion program questions from previous lectures - quick sort - 40

# todo: hw: time and space complexity of all recursion program questions from previous lectures - subsets - 41

# todo: hw: time and space complexity of all recursion program questions from previous lectures - subsequences - 41

# todo: hw: time and space complexity of all recursion program questions from previous lectures - keypad - 42

# todo: hw: time and space complexity of all recursion program questions from previous lectures - permutations swapping - 43

# todo: hw: time and space complexity of all recursion program questions from previous lectures - permutations no swapping - 43

# todo: hw: time and space complexity of all recursion program questions from previous lectures - ratmaze - 44

# todo: hw: learn master's theorom and solve questions related to it - https://www.codingninjas.com/codestudio/guided-paths/competitive-programming/content/126222/offering/1476042
