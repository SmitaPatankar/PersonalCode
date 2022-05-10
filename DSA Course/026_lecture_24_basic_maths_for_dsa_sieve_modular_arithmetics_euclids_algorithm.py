# prime number details
"""
number that has no other divisors except 1 and itself
i.e. dividing with any number other than 1 and itself doesn't give remainder as 0
any number <=1 is not a prime number
O(n) time complexity
To find all numbers less than n that are prime, almost O(n^2) complexity
Hence, below optimized solution.
"""

# todo: hw: not mandatory: math: learn how harmonic progression of prime number related to taylor series is O(log(logn)) time complexity
# program: https://leetcode.com/problems/count-primes/ using sieve of erastothenes
# logic:
# set count as 0
# have an array with all numbers from 0 to n-1 marked as Prime
# mark 0 and 1 as not prime
# loop from 2 to n-1
# we know that 2 is not prime, loop over all its multiples and mark them not prime ans also increase count by 1 to store 2 as prime number
# check 3, it is prime as none of the numbers before it were its divisors thats why it was not crossed, increase count, loop pver and mark multiples not prime ans so on...
# complexity - first we marked n/2 numbers as not prime, n/3, n/5 so on
# n(1/2 + 1/3 + 1/5 + ...)
# O(n*log(logn)) time complexity
"""
def count_prime_numbers(n):
    a = [True] * n
    a[0] = False
    a[1] = False
    count = 0
    for i in range(2, n):
        if a[i] == True:
            print(i, end=" ")
            count += 1
            for j in range(2*i, n, i):
                if j % i == 0:
                    a[j] = False
    print()
    return count
print(count_prime_numbers(100))
"""

# todo: check why max root r is taken as 1000001
# hw: understand segmented sieve
# program: segmented sieve - count prime numbers
# count prime numbers between given start and end
# we cant start from 2 and use simple sieve as it will run out of memory
# we can make array for given range though
# will mark multiples of 2 to squareroot of end as false squareroot of end will be much smaller than end so we can use that
# eg: 20 to 50 - mark all multiples of primes between 2 and 7 i.e. multiples of 2,3,5,7 remaining are 23,29,31,37,41, 43, 47
# eg: max multiple of 36 will be 6 only coz 6*6 if we need one to bigger like 9 then other will be smaller like 4 which will already be covered
# make a sieve to store prime numbers from 2 to root end also and make an array of only primes till root n
# to save time we added 2 and then just looped over odd numbers and added
# program logic:
# one sieve for 2 to root end and find primes
# other series from start to end find primes i.e. multiples of above
# logic for filling segmented sieve we need to step on multiples of say 2 or 3 or 5 etc
# for finding closest multiple on or before start do ((start/i) * i)
# eg: (24/5)*5 i.e. 20 it is smaller so add 5 i.e 25
"""
def form_sieve():
    n = 1000001
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n):
        if is_prime[i] == True:
            for j in range(2*i, n, i):
                is_prime[j] = False
    return [i for i in range(len(is_prime)) if is_prime[i] is True]
def print_primes(l, r, primes):
    n = r-l+1
    ans = [True] * n
    for i in range(len(primes)):
        current_prime = primes[i]
        if current_prime * current_prime <= r:
            base_value = (l//current_prime) * current_prime
            if base_value < l:
                base_value += current_prime
            # my code - start
            if base_value == 0:
                base_value += current_prime
            if base_value == current_prime:
                base_value += current_prime
            # my code - end
            for j in range(base_value, r+1, current_prime):
                ans[j-l] = False
        else:
            break
    if l == 0:
        ans[0] = False
        if r >= 1:
            ans[1] = False
    elif l == 1:
        ans[0] = False
    print([i+l for i in range(n) if ans[i] is True])
def main():
    primes = form_sieve()
    no_of_tcs = int(input("enter no. of TCs-->"))
    while no_of_tcs:
        l = int(input("enter leftmost value of range-->"))
        r = int(input("enter rightmost value of range-->"))
        print_primes(l,r,primes)
        no_of_tcs -= 1
main()
"""

# GCD/HCF details
"""
greatest common divisor
highest common factor
maximum number that divides each of the given 2 numbers and returns 0
eg: 24 and 72 --> 24
brute force approach:
24  = 2 x 2 x 2     x 3
72  = 2 x 2 x 2 x 2 x 3
ans = 2 x 2 x 2     x 3 = 24
time complexity is huge
Hence, below optimized solution.
"""

# todo: revise
# program: Euclid's algorithm for GCD/HCF - https://www.codingninjas.com/blog/2020/07/25/explained-euclids-gcd-algorithm/
# logic: gcd(a,b) = gcd(a-b,b) or gcd(a,b) = gcd(a%b,b)
# eg: gcd(72,24) = gcd(0,24) = 24
# eg: gcd(74,24) = gcd(2,24) i.e. gcd(24,2) = gcd(0,2) i.e. 2
# logic: keep doing till atleast one parameter becomes 0 and then other parameter is the ans
# program logic: if a is 0 return b, if b is 0 return a, else while a anb b are not equal, keep subtracting bigger one from smaller one and return smaller one at the end coz bigger one would be 0
# euclid's algo proof
# if d divides x and y, d*a = x, d*b = y, x-y = d*a - d*b i.e. d*(a-b) that means divisor of x and y is also divisor of x and y
# O(Log min(a, b)) time complexity
"""
def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
    return a  # because bigger will be 0 towards the end so smaller is the ans
print(gcd(24,72))
print(gcd(72,24))
print(gcd(74,24))
"""

# todo: math: learn more: binary euclids formula and complexities compared to int: https://www.codingninjas.com/blog/2020/07/25/explained-euclids-gcd-algorithm/
# hw: understand binary eucledian algorithm - https://www.codingninjas.com/blog/2020/07/25/explained-euclids-gcd-algorithm/
# if both are same, return result * one of them
# elif both are even return gcd of their half and multiply 2 to ans
# else if one of them is divisible to by 2, return gcd of that half and other full
# else if one is greater than other, return gcd of difference and smaller number
# binary operations work in linear time, even for big integers
"""
def gcd(a,b,res):
    if a == b:
        return a * res
    elif a % 2 == 0 and b % 2 == 0:
        return gcd(a//2,b//2,2*res)
    elif a%2 == 0:
        return gcd(a//2, b, res)
    elif b%2 == 0:
        return gcd(a, b//2, res)
    elif a>b:
        return gcd(a-b, b, res)
    else:
        return gcd(b-a, a, res)
print(gcd(12,6,1))
"""

# todo: learn euclidean extended algorithm more and all euclid complexities - https://www.codingninjas.com/blog/2020/07/25/explained-euclids-gcd-algorithm/
# hw: understand extended euclidean algorithm - https://www.codingninjas.com/blog/2020/07/25/explained-euclids-gcd-algorithm/
# gives 2 coefficients x and y along with gcd such that ax+by = gcd(a,b)
# uses % for gcd
# produces results for -ve ints also
"""
def gcd(a,b,x,y):
    if b == 0:
        x = 1
        y = 0
        print(f"x {x}")
        print(f"y {y}")
        return a
    x1 = 0
    y1 = 0
    d = gcd(b, a%b, x1, y1)
    x = y1
    y = x1 - y1 * (a//b)
    print(f"x {x}")
    print(f"y {y}")
    return d
print(gcd(35,15,0,0))
"""

# hw: program: Program to find the LCM of two numbers using GCD. - https://www.codingninjas.com/blog/2020/07/25/explained-euclids-gcd-algorithm/
# brute force - find prime factors of both and take their union and product
# better logic: lcm(a,b) = a*b/gcd(a,b)
"""
def gcd(a,b):
    if a == 0:
        return b
    else:
        return gcd(b%a, a)
def lcm(a, b):
    gcd_ = gcd(a,b)
    lcm_ = (a//gcd_) * b
    return lcm_
print(lcm(15,9))
"""

# todo: revise
# todo: program: check why 0.001 is used and fix program for all edge cases
# hw: program: Program to find GCD of floating-point numbers. - https://www.codingninjas.com/blog/2020/07/25/explained-euclids-gcd-algorithm/
# logic: if b is greater, perform gcd on b,a, if b < 0.001 return a, else perform gcd on a-b, b
# logic: to avoid subtracting small number again and again from large number
# we are calculating the amount to be subtracted as how many times it is completely divisible by b
# i.e. subtract math.floor(a/b)*b from a
"""
def gcd(a,b):
    if b > a:
        print(f"{a} {b}")
        return gcd(b, a)
    elif b <= 0.001:
        return a
    else:
        return gcd(a-math.floor(a/b)*b, b)
a = 33.15
b = 22.45
print("{0:.2f}".format(gcd(a,b)))
"""

# hw: program: Program to find the common ratio of three numbers. - https://www.codingninjas.com/blog/2020/07/25/explained-euclids-gcd-algorithm/
# logic: 3:4 8:9 multiply first ratio b 8 and second ration by 4 to make the middle term common
# then divide everything by math.gcd
"""
def common_ratio(a,b1,b2,c):
    a = a*b2
    b = b1*b2
    c = c*b1
    gcd = math.gcd(math.gcd(a,b),c)
    a = a//gcd
    b = b//gcd
    c = c//gcd
    return f"{a}:{b}:{c}"
print(common_ratio(3,4,8,9))
"""

# hw: program: Program to find GCD of an array of integers. - https://www.codingninjas.com/blog/2020/07/25/explained-euclids-gcd-algorithm/
# logic for gcd, if  is 0 return a
# else perform gcd on b, a%b --> to put bigger and smaller in sequence
# keep finding gcd of first 2 numbers and that with the third number that with fourth so on
"""
def find_gcd(a,b):
    if b == 0:
        return a
    else:
        return find_gcd(b, a%b)
def gcd_array(arr):
    a = arr[0]
    b = arr[1]
    gcd = find_gcd(a,b)
    for i in range(2, len(arr)):
        gcd = find_gcd(gcd, arr[i])
    return gcd
print(gcd_array([9,15,30]))
"""

# todo: math: see how n(n+1)/2 leads to sum of n numbers and how n(n+1)(2n+1)/6 leads to squares of n numbers
# hw: program: Program to find the sum of squares of N natural numbers. - https://www.codingninjas.com/blog/2020/07/25/explained-euclids-gcd-algorithm/
# logic: sum of first n numbers i.e. 1,2,3,4,5 = n(n+1)/2 i.e. 5(6)/2 i.e. 15
# logic: sum of first n squares i.e. 1,2,3,4,5 = n(n+1)(2n+1)/6 i.e. 5(6)(11)/6 = 55 i.e. 1+4+9+16+25 = 55
"""
def first_n_squares(n):
    return n*(n+1)*((2*n)+1)//6
print(first_n_squares(5))
"""

# hw: LCM and GCD relation - https://www.codingninjas.com/blog/2020/07/25/explained-euclids-gcd-algorithm/
# logic: LCM(a,b) * GCD(a,b) = a*b

# todo: math: check why lcm and gcd product leads to product of numbers always
# todo: math: check how to calculate p/q and return r such that r.q mod m = p mod m
# todo: math: check why -8 % 7 == 6
# todo: math: check why a^m mod m = a mod m when m is prime
# todo: math: revise fermat's little theorom and its complexities
# todo: math: learn https://en.wikipedia.org/wiki/Euler%27s_totient_function
# todo: program: https://codeforces.com/blog/entry/72527?f0a28=2: https://codeforces.com/contest/1281/problem/C
# todo: program: https://codeforces.com/blog/entry/72527?f0a28=2: https://codeforces.com/contest/1279/problem/D
# todo: program: https://codeforces.com/blog/entry/72527?f0a28=2: https://codeforces.com/contest/1178/problem/C
# todo: program: https://codeforces.com/blog/entry/72527?f0a28=2: https://codeforces.com/contest/1248/problem/C
# todo: program: https://codeforces.com/blog/entry/72527?f0a28=2: https://codeforces.com/contest/935/problem/D
# todo: program: https://codeforces.com/blog/entry/72527?f0a28=2: https://codeforces.com/contest/300/problem/C
# hw: understand modulo properties basics: https://codeforces.com/blog/entry/72527?f0a28=1
"""
a % n will always lie in range of 0 to n-1 because rest of the portion will anyways get divided quotient no. of times

some questions tell to print ans in form of (10^9 + 7)
to avoid overflow eg: for 20 factorial

(a+b) % m = ((a % m) + (b % m)) % m
(a-b) % m = ((a % m) - (b % m)) % m
(a*b) % m = ((a % m) * (b % m)) % m

we can always store residues this way

in some problems we have to calculate p/q and return r such that r.q mod m = p mod m

n % m actually means n - (n/m) times m

-8 % 7 == 6 not -1

expr1≡expr2(modm) means expr1 mod m = expr2 modm

modular multiplicative inverse of a is a^-1 such that a*a^-1 = 1

fermat's little theorom
as far as m is prime,
a^m mod m = a mod m
a^m-1 mod m = 1
a.a^m-2 mod m = 1
find a^m-2 mod m
a^−1=a^m−2 mod m 
works when a mod m is not zero

m-2 power takes long
hence, if x is even, x^n = (x^2)^n/2 and if x is odd x^n = x(x^2)^(n-1)/2

a/b  mod m=a⋅b−1  mod m

combinatorics (n r) i.e. n!/(n-r)!r! can be done is modulo

3=4x+5  mod 109+7  can be done as x=−1/2  mod 10**9+7

for x^n mod m cant do n mod m, hence use φ(m) i.e. euler's toient function
If m is prime, φ(m)=m−1 this may not be prime

0^0 is 1, 0φ(m) is 0
"""

# hw: program: recursive power: https://codeforces.com/blog/entry/72527?f0a28=1
"""
def power(x, n, m):
    if n == 0:
        return 1
    elif n % 2 == 0:
        ans = power(x, n//2, m)
        return (ans * ans) % m
    else:
        ans = power(x, n//2, m)
        return (ans * ans * x) % m
print(power(2, 5, 3))
"""

# hw: program: iterative power: https://codeforces.com/blog/entry/72527?f0a28=1
"""
def power(x, n, m):
    ans = 1
    while n > 0:
        if n % 2 == 0:
            x = (x*x) % m
            n = n/2
        else:
            ans = ans * x % m
            n -= 1
    return ans
print(power(2, 5, 3))
"""

# todo: revise
# program: https://www.codingninjas.com/codestudio/problems/modular-exponentiation_1082146 - fast exponentiation
# for a^b we had to multiply a to ans b times i.e. O(b) time complexity
# Hence, use fast exponentiation for O(logb) time complexity
# a^b can be shown as (a^2)^b/2 if b is even else (a^2)^b/2 * a if b is odd
# question: return (x ^ n) % m
# logic bit operations are less expensive compared to divide
# so better to do &1 for checking odd and better to do >> 1 for divide by 2
# program logic: square number everytime to reduce operations needed by half, stop when operations needed become zero
# number is stored in ans when no. of operations is odd, so it is anyways stored at end for 1
# for odd numbers keep one extra number multiplied to ans as when we do //2, remainder 1 goes away
# always keep doing %m, extra mods dont harm
"""
def power(x, n, m):
    res = 1
    while n > 0:
        if n & 1:  # odd
            res = (res * (x%m))%m
        x = ((x%m) * (x%m))%m
        n = n >> 1
    return res
print(power(4,9,10))
"""

# hw: math: pigeon hole principe understanding
"""
if there are n pigeons and n-1 holes, there will atleast be one hole where more than one pigeons enter

application: if a drawer has infinite socks of 4 colours, how many socks need to be picked minimum for one same colour pair to form - 5
pigeon hole principle: n socks and n-1 colours that means 1 sock is of repeat colour

set has 1,2,3,4....2n
eg: n=4 {1,2,3,4,5,6,7,8}
pick any n+1 numbers then atleast one pair will have sum as 2n+1
eg: atleast one pair from selected 5 numbers will have sum 9
pairs are like 18, 27,36,45 - 4 pairs
we'll pick one number from each pair, still we'll have to pick one more number that will form a whole pair
5 picked numbers present in 4 pairs that means atleast one pair has both our picked numbers

n people in group
each person can make as many friends
atleast 2 people will have same friend count
eg: 10 people
people can make friends count of 0 to 9
but, if one person made 0 friends, then other people can also make max 8 friends only
and, if all people make some friends then each person will have atleast one friend i.e. min 1 and max 9 friends
so possible counts of friends are any 9 only and people are 10
that means 2 people have same friend count

undirected graph with atleast 2 vertex
there will atleast be 2 vertext whose degree is same
degree means no of edges
degree of a vertex can be from 0 to number of vertexes i.e. v -1
eg:
4 vertexes
each vertex degree can be between 0 to 3
but, if one vertex has degree 0 then others can have 0 to 2 only
so either way, each vertex can have degree between either 0 to 2 or 1 to 3
4 vertexes and 3 options for degrees
thats y 2 vertexes will have same degree

equilateral triangle
size 2
make 5 points inside it
atleast 2 points will be there between which max distance possible is 1
when we join midpoints of eq triangle, all sides of internal and external triangles become 1
there are 4 internal triangles and 5 points that means two points one one inner triangle
that means max distance 1

51 friends circle
1 friend doesnt like max 3 friends
how many min groups needed such that people disliking each other dont come in same group?
1 person dislikes 3 people and he is also disliked by 3 people
so all these 7 ppl should be in diff groups
"""

# todo: try to run it on codechef
# hw: math: program: pigeon hole principle few questions - https://www.codechef.com/problems/GRAYSC
# logic:
# eg: 1   0   2   3   7
# eg: 01  00  10  11  111
#
# Array of size n of positive integers
# array elements between 0 and 2^64
# every adjacent numbers have one digit different in binary representation
# find if there exists 4 numbers such that their xor is 0 and they are adjacent
# size of array is between 1 and 100000
#
# observation:
# since the adjacent elements differ by one bit only their xor will have 1 set bit only because xor of 0 and 1 is 1
# a[i1] ^ a[i2] = a[i3] ^ a[i4]
# numbers < 2^64 - i.e. max 64 set bits
# xor can have set bit at any one of the 64 positions
# 64 possibilities for xor
#
# so adjacent numbers xor can be between 1 and 11111....
# create set of xors of all adjacent numbers
#
# pigeon hole principle
# since there are only 64 possibilities for xors of adjacent numbers,
# if there are more than 128 numbers, atleast one xor will repeat and they will cancel out and become 0 - pigeon hole principle
#
# i1 i2 i3 loop for less than 129 i.e. N^3
# i4 anywhere ahead i.e. N
# naive
#
# smart
# save count of all elements
# decrement count if same as i1 i2 i3 then if >=1 is remaining, we have found a[i1]^a[i2]^a[i^3] match in i4
"""
from collections import defaultdict
def func():
    print("taking array size as input")
    n = int(input())
    print("taking space separated array elements as input")
    arr = list(map(int, input().split()))

    if n >= 129:
        print("xor of adjacent elements with only 1 bit difference will always have 1 set bit i.e. 64 possible locations for set bits")
        print("more than 128 elements i.e. 64 pairs result into atleast one duplicate xor i.e. a[i1]+a[i2] = a[i3]+a[i4]")
        return True

    print("saving count of each element so that we can use it later to find a[i4] that is equal to looped a[i1] ^ a[i2] ^ a[i3]")
    d = defaultdict(int)
    for element in arr:
        d[element] += 1

    print("looping to get a[i1] ^ a[i2] ^ a[i3] and then checking if the value exists in above saved count of elements")
    for i in range(0, len(arr)-2):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                xor = arr[i] ^ arr[j] ^ arr[k]
                print(f"{arr[i]} ^ {arr[j]} ^ {arr[k]} is {xor}")
                count = d[xor]
                print("checking if xor of first 3 elements exists as 4th element, don't count if a[i1] or a[i2] or a[i3] is same")
                if arr[i] == xor:
                    count -= 1
                if arr[j] == xor:
                    count -= 1
                if arr[k] == 1:
                    count -= 1
                if count >= 1:
                    print("found")
                    return True
    print("not found")
    return False
print(func())
"""

# todo: revise
# todo: submit on spoj and verify
# hw: math: program: pigeon hole principle few questions - https://www.spoj.com/SZTE11T1/problems/HALLOW/
# each neighbour wants to give limited sweets on halloween
# children will take all sweets n divide
# children want to select neighbours such that each kid gets equal sweets
# they don't want any sweets left that are undivided
#
# children are between 1 and 100000
# neighbors are between 1 and 100000
# children are <= neighbors
# array of no of sweets given by each neighbor - sweets between 1 to 100000
#
# eg: c n chocs --> indices of neighbors
# 4 5
# 1 2 3 7 5
# ans: 3 5
# ans: no sweets for negative
# ans: any one of many solutions
#
# logic:
# sum of sweets should be multiple of no of children
# each neighbor gives atleast one sweet
# children are <= neighbor
# each child will get atleast one sweet
# sum must be equal to c or multiple of c if more
# i.e. remainder should be 0
# there are c possible remainders
# n >= c
# that means 2 similar remainders
# make prefix sum array
# eg: [1,2,3,7,5] --> [1,3,6,13,18]
# if remainder 0 is found for any sum, return all indexes till that
# else: only c-1 remainders are possible
# that means atleast 1 remainder repeats
# remainders -> [1,3,6,13,18] -> [1,3,2,1,2]
# for similar remainder, sum of all numbers between them is multiple of c i.e. has modulus 0
#
# here remainder is 1 at 2 places
# that means if we remove one of those places, remainder will no longer be 1 and be 0
# we have to remove the smaller one, because that could be the remainder itself whereas the greater one is more
"""
def func(c, n, arr):
    pfa = []
    for i in range(n):
        if i == 0:
            pfa.append(arr[i])
        else:
            pfa.append(arr[i] + pfa[i-1])
    for i in range(n):
        if pfa[i] % c == 0:
            return [x for x in range(1, i+2)]
    for i in range(n-1):
        for j in range(i+1, n):
            if pfa[i] % c == pfa[j] % c:
                return [x for x in range(i+2, j+2)]
s = input()
c = int(s.split(" ")[0])
n = int(s.split(" ")[1])
s = input()
arr = list(map(int, s.split(" ")))
ans = func(c, n, arr)
if isinstance(ans, list):
    s = ""
    for i in range(len(ans)):
        if i == 0:
            s += str(ans[i])
        else:
            s += " "
            s += str(ans[i])
    print(s)
else:
    print("no sweets")
"""

# todo: submit on tool and verify
# hw: math: program: pigeon hole principle few questions - divisible sub arrays - https://hack.codingblocks.com/app/practice/6/p/266
# array having n elements
# find no. of arrays where sum of elements is divisible by n
# array means continuous
#
# eg: [1,3,2,6,4]
# ans: 5
#
# n is between 1 and 10^5
# elements <= 10^9
#
# logic:
# n elements' mod should be 0
# mod can only be between 0 and n-1
# so atleast two elements will have same mod
# cumulative sum array eg: [1,4,6,12,16]
# b % n - a%n should be 0 i.e. b%n = a % n
# remainders: eg: [1,4,1,2,1]
# from all indexes where remainder is sum, we can choose any 2 positions to form a sub array excluding the initial element
# so nC2 sums for each duplicate remainder is the ans
# frequencies of remainders - [0,3,1,0,1]
"""
def main():
    # get no. of tcs
    t = int(input())
    # loop over each tc
    for i in range(t):
        # take no of elements in array
        n = int(input())
        # make empty array for elements
        a = [0] * n
        # make empty array for remainder frequencies of cumulative sum
        remainders_frequency = [0] * n
        # set 0's frequency as 1 because even if we get one more zero, we have to have an array till there
        remainders_frequency[0] = 1
        # make initial sum as 0
        sum = 0
        for j in range(n):
            # take element of array
            a[j] = int(input())
            # make it positive if negative for proper mod anyways we care of remainder itself
            if a[j] < 0:
                a[j] += n
            # add element to cumulative sum
            sum = sum + a[j]
            # add 1 to remainders frequency for current sum's remainder
            remainders_frequency[sum%n] += 1
            sum = sum % n
        ans = 0
        for sum_frequency in remainders_frequency:
            if sum_frequency >= 2:
                ans += (sum_frequency * (sum_frequency - 1))//2
        print(ans)
main()
"""

# todo: practice
# todo: catalan triangulation for dp
# hw: math: understand catalan number (series) and its real life application (tbd: used in binary search tree)
"""
people sitting on round table
there should be even number of people so that no one is left out
in how many ways can they shake hands without crossing each other's hands
2 people - 1 way
4 people - 2 ways
6 people - 5 ways

draw mountain
single up and down line - one mountain
two lines - up down up down or up up down down i.e. 2 ways
3 strokes - 5 ways

give ans to many questions in math

1,2,5,14,42,132,....

formula:
(2n)!/n!(n+1)!
eg: 3 --> 5

we can recover handshakes from mountains and vice versa i.e. bijection
questions are same

catalan series for n - c0cn-1 + c1cn-2 + c2cn-3 .... + cn-1c0

applications:
- no of binary search trees that can be formed from given no. of nodes - Cn
- ways of arranging parentheses
    () - 1 way
    ()() or (()) - 2 ways
    ()()() or ()(()) ----- (())() ----- (()()) or ((())) - 5 ways - 0 inside 3 outside, 1 inside 1 outside, 2 inside 0 outside i.e. c0c2, c1c1, c2c0
- dyck words - arrange x and ys such that ys are not greater than x from initial position
    xy - 1
    xxyy xyxy - 2 ways put one x y and other inside or outside
    xxyxyy xxxyyy xxyyxy xyxyxy xyxxyy - 5 ways
- grid with n rows and n columns - go from bottom to top such that we stay below the diagonal - more h and less v means below same as dyck words - same as rotated mountain grid
- ways of converting polygon i.e. no of vertices into triangles - cn-2
    0 --> 0
    1 --> 0
    2 --> 0 --> c0
    3 --> 1 --> c1
    4 --> 2 triangles --> c2
    5 --> see vertices left on each side after making one triangle somewhere --> c3
- connect points on circle such that they do not cross each other - connect a pair and see how many are left

catalan series - put 1 and arrange the rest as per previous

c0 and c1 are 1 and calculate the rest
"""

# todo: optimize using dp
# hw: program: catalan number
"""
def catalan(n):
    if n in [0,1]:
        return 1
    res = 0
    # c3 = c0c2 + c1c1 + c2c0
    for i in range(n):
        res += (catalan(i) * catalan(n-i-1))
    return res
def main():
    for i in range(10):
        print(catalan(i))
main()
"""

# hw: math: understand inclusion exclusion principle
"""
a union b = a + b - a intersection b
a union b union c = a + b + c - a intersection b - a intersection c - b intersection c + a intersection b intersection c

for finding no of ways to do something

inclusion exclusion principle - include both and exclude double
"""

# hw: math: program: inclusion exclusion principle - nos divisible by 5 or 7
# logic: n/a + n/b - n/a*b
"""
def func(n, a, b):
    return (n//a) * (n//b) - (n//(a*b))
print(func(1000, 5, 7))
"""

# hw: program: factorial of a number using %m without overflow - m = 10**9 + 7, n = 212
"""
def factorial(n, m):
    ans = 1
    for i in range(2, n+1):
        ans = (ans * (i%m)) % m
    return ans
print(factorial(212,(pow(10,9)+7)))  # 616613957
"""

# tbd: math: crt
# tbd: math: locust
# tbd: math: FL
# tbd: math: probability
# tbd: math: euler's function
