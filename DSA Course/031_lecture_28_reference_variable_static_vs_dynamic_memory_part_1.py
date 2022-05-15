# cpp reference variable
# todo: python: check if pass by value can be done
"""
same memory block with diff names

reference variable is used as function parameters to avoid pass by value where original value doesnt get changed
we can also return reference variables from function bu thats bad practice as that is local someone else may change that memory block later or it may become inaccessible
"""

# todo: python: check how stack and heap memory is used
# todo: computers: learn what is 64 bit and 32 bit system
# todo: hw: cpp: read this doc completely, void pointer, address typecasting(notimp) https://www.codingninjas.com/codestudio/guided-paths/basics-of-c/content/118785/offering/1381146
# cpp memory allocation - static and dynamic - stack and heap - compile time and run time
"""
don't take array size as input and then make array because that is runtime not compile time, hence make big array at start
program start has small stack and big heap memory, we need more stack memory hence define array size already else program will crash
int, char, array etc gets created in stack memory
hence, use heap memory for creating stack with input size
stack - static memory allocation
heap - dynamic memory allocation
use pointer to access the memory block created in heap memory - pointer is stored in stack
pointer takes 8 byte in 64 bit system and 4 byte in 32 bit system
total 9 bytes for a char i.e. 8 bytes for pointer and 1 for actual value
same for dynamic arrays
dynamic takes extra memory for pointer
memory gets released at end of each iteration of while loop for defined variables
heap memory wont be free outside while loop
manually release memory in heap
"""