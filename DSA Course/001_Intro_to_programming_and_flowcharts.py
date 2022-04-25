# problem solving steps
"""
- understand problem
- note given values
- form approach - flow chart i.e. diagramatic/pseudo code i.e. written generic rough code or logic i.e. language independent
- write program - in high level language - source code
- convert program to machine understandable format i.e. 1s and 0s
"""

# flow chart components
"""
- terminator - start/stop
- parallelogram - input/output eg: a = input() eg: print(a) - memory blocks are made with name and value
- rectangle - process - eg: i = i + 1
- diamond - decision making i.e. condition - eg: if i > 0 - outputs into yes/no
- arrows - flow and connection
- TBD: circle - connector - for functions
"""

# flow chart / pseudocode: sum
"""
start
input a, b
sum = a + b
print sum
stop
"""

# flow chart / pseudocode: simple interest - logic: si = p * r * t / 100
"""
start
input p, r , t
si = p * r * t / 100
print si
stop
"""

# flow chart / pseudocode: average
"""
start
input a,b,c
avg = a + b + c / 3
print avg
stop
"""

# flow chart / pseudocode: a less than b
"""
start
input a, b
if a < b
    print True, go to stop
else
    print False, go to stop
stop
"""

# flow chart / pseudocode: odd/even
"""
start
input n
if n % 2 is 0
    print even, go to stop
else
    print odd, go to stop
stop
"""

# flow chart / pseudocode: +ve/-ve/0
"""
start
input n
if n > 0:
    print positive, go to stop
else:
    if n < 0:
        print negative, go to stop
    else:
        print 0, go to stop
stop
"""

# hw: flow chart / pseudocode: valid triangle - logic: any 2 sides sum > third side
"""
start
read a, b, c
if a+b > c:
    print valid, go to stop
else:
    if b + c > a:
        print valid, go to stop
    else:
        if a + c > b:
            print valid, go to stop
        else:
            print invalid, go to stop
stop
"""

# flow chart / pseudocode: print one to n flow chart/pseudo code
"""
start
read n
seq = 1
if seq <= n:
    print seq
    seq = seq + 1
    loop back to if
else:
    stop
"""

# flow chart / pseudocode: print even numbers from 1 to n(excluded) - logic: start from 2 and keep adding 2 until exceeds n
"""
start
read n
seq = 2
if seq < n:
    print seq
    seq = seq + 2
    loop back to if
else:
    stop
"""

# hw: flow chart / pseudocode: print odd numbers from 1 to n - logic: start from 1 and keep adding 2 until exceeds n
"""
start
read n
seq = 1
if seq <= n:
    print seq
    seq = seq + 2
    loop back to if
else:
    stop
"""

# flow chart / pseudocode: sum from 1 to n
"""
start
input n
seq = 1
sum = 0
if seq <= n:
    sum = sum + seq
    seq = seq + 1
    loop back to if
else:
    print sum
    stop
"""

# hw: flow chart / pseudocode: factorial - logic: 5! = 5*4*3*2*1
"""
start
input n
factorial = 1
if seq > 1:
    factorial = factorial * seq
    seq = seq - 1
    loop back to if
else:
    print factorial
    stop
"""

# flow chart / pseudocode: check prime - logic: doesnt have remainder 0 for anything between 2 and n-1
"""
start
input n
seq = 2
if seq < n:
    if n % seq == 0:
       print not prime, go to stop
    else:
        seq = seq + 1
        loop back to if
else:
    print prime
stop
"""

# todo: python: difference between compiler and interpreter
# programming language details
"""
- to instruct computer to perform tasks
- has rules
- needs compiler in between to convert source code to binary language i.e. 1s and 0s for computer to understand i.e. executable file for computer to run
- compiler helps in finding errors also - compile time and run time
"""

# IDE details
"""
- integrated development environment for writing and executing code
- eg: vscode etc
- install / use online
"""
