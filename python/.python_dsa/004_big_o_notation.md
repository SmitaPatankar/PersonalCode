- [notations](#notations)
- [time complexities (good to bad)](#time-complexities-good-to-bad)
- [space complexity](#space-complexity)
- [drop constants and non dominant terms](#drop-constants-and-non-dominant-terms)
- [calculate time complexity of code](#calculate-time-complexity-of-code)

# notations
- big o - worst - eg: to search sequentially - time complexity is O(N)
- big omega - best - eg: to search sequentially - time complexity is omega(1)
- big theta - average of best and worst - eg: to search sequentially - time complexity is theta(N/2)

# time complexities (good to bad)
increase in time as per increase in size of input

- O(1) - constant
eg: accessing an element in array
eg: selecting a card from deck randomly

- O(log N) - logarithmic time
eg: visit specific elements in array
eg: select specific card from sorted deck that can be splitted as relevant and irrelevant multiple times
eg: binary search in sorted array - each time array is divided by 2 until we reach 1 - for 16 elements it is divided 4 times to get 1 i.e. 1 and how many times 2 will give 16 i.e. 2 raised to what is 16 i.e. log of 2^16

- O(N) - linear
eg: visit every element in array
eg: searching specific card in deck

- O(N log N) - LEARN MORE

- O(N^2) - quadratic
eg: nested loops on same array
eg: for each picked card number, find all its colors

- O(2^N) - exponential - doubles with each addition to input set
eg: double recursive fibonnaci function

- O(N!) - LEARN MORE

# space complexity
increase in required memory as per increase in size of input
eg: recursive function for sum of elements in array i.e. O(N)
eg: sequence of sum of pairs of adjacent numbers upto number i.e. O(1)

# drop constants and non dominant terms
because they wont matter much and will be very small as input grows
eg: o(2N) -> O(N)
eg: O(N^2 + N) = O(N^2)
eg: O(N + logN) = O(N)
eg: O(2 * 2^N + 1000N^100) = O(2^N)

# calculate time complexity of code
measure for each line
