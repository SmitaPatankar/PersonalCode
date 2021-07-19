"""
sorting and indexing data
index data with keys created from formulas

search in O(1) in best and O(N) if many collissions using same formula

hash function: map data of arbitrary size to data of fixed size
hash value: returned by hash function
key: input data by user
hash table: map key to value
collision: multiple keys produce same output for hash function

hash functions:
eg: mod no of cells i.e. reduce to limited size for table i.e. array
eg: sum of ascii value of letters mod no of cells in table
distribute values uniformly in table
use all input data

collision resolution:
    direct chaining: hash table has hash value and linked lists with keys
    open addressing: store in other cells
        linear probing - closest following cell
        quadratic probing - 2, 2+1square, 2+2square
        double hashing - hash key with diff func and sum the cell numbers - if still collide 1st + 2*2nd and so on

table full:
direct chaining: not possible
open addressing: create 2x table and performing hashing again on current keys

directchaining:
for frequent deletion as there are not many empty cells

open adrressing:
when size is known as no resizing

security because password hash cant be converted back to password only viceversa
file paths mapped to memory location using hash functions

used in dictionary
"""