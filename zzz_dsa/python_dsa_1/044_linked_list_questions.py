# remove duplicates from unsorted linked list
# -------------------------------------------
# start looping over all elements and add one by one to visited set
# if next one is duplicate, delete it
# else loop further
# -------------------------------------------
# time = O(n)
# space = O(n)
# -------------------------------------------
# loop over all elements
# start loop over all elements beginning from there internally
# if next one is duplicate, delete it
# else loop further
# ---------------------------------------------
# time = O(n)
# space = O(1)

c = __import__("043_custom_ll")

def removeduplicates_one(ll):
    if not ll.head:
        return
    currentnode = ll.head
    visited = set([currentnode.value])
    while currentnode.next:
        if currentnode.next.value in visited:
            currentnode.next = currentnode.next.next
        else:
            visited.add(currentnode.next.value)
            currentnode = currentnode.next
    return ll

def removeduplicates_two(ll):
    if not ll.head:
        return
    currentnode = ll.head
    while currentnode:
        runner = currentnode
        while runner.next:
            if runner.next.value == currentnode.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        currentnode = currentnode.next
    return ll.head

cll1 = c.CustomLL()
cll1.generate(10, 0, 5)
print(cll1)
removeduplicates_one(cll1)
print(cll1)

cll2 = c.CustomLL()
cll2.generate(10, 0, 5)
print(cll2)
removeduplicates_two(cll2)
print(cll2)

# return nth element from singly linked list
# ------------------------------------------
# create one pointer at start
# create other pointer at nth elememnt from start
# move both pointers till the 2nd one reaches end
# that is when the first one would have reached nth position from start

def nthtolast(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head
    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

cll = c.CustomLL()
cll.generate(10,0,99)
print(cll)
print(nthtolast(cll, 3))
print(nthtolast(cll, 11))

# partition linkedlist around a value x such that LHS contains <x and RHS contains >= x
# -------------------------------------- 
# make currentnode as first element
# point tail also to it
# make its next as null
# i.e. small LL with only one element
# then traverse through rest of the elements
# if smaller than x, put on left else on right as per standard process
# --------------------------------------
# time = O(n)
# space = O(1)
# --------------------------------------
# learn more for first iteration

def partition(ll, pivot):
    curnode = ll.head
    ll.tail = ll.head
    while curnode:
        nextnode = curnode.next
        if curnode.value < pivot:
            curnode.next = ll.head
            ll.head = curnode
        else:
            ll.tail.next = curnode
            ll.tail = curnode
        curnode = nextnode
    if ll.tail.next is not None:
        ll.tail.next = None
    return ll

cll = c.CustomLL()
cll.generate(10,0,50)
print(cll)
print(partition(cll, 30))

# ll1 - 7 -> 1 -> 6
# ll2 - 5 -> 9 -> 2
# outputll - 617 + 295 i.e. 912 i.e. 2 -> 1 -> 9
# -------------------------------------- 
# sum each positions element from each list along with the carry from previous sum
# and add to new ll
# note: loop until both lists are empty
# --------------------------------------
# time = O(n)
# space = O(n) for new ll
# --------------------------------------
# learn more for first iteration

def sumll(lla, llb):
    n1 = lla.head
    n2 = llb.head
    carry = 0
    ll = c.CustomLL()
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.add(int(result % 10))
        carry = int(result / 10)
    if carry>0:
        ll.add(int(carry))
    return ll

ll1 = c.CustomLL()
ll1.add(7)
ll1.add(1)
ll1.add(6)
ll2 = c.CustomLL()
ll2.add(5)
ll2.add(9)
ll2.add(2)
print(ll1)
print(ll2)
print(sumll(ll1, ll2))

# find intersecting node from 2 LL by reference not value
# 3 -> 1 -> 5 -> 9 ->
#                      7 -> 2 -> 1 
#       2 -> 4 -> 6 -> 
# output should be 7
# ---------------------------------------------------------
# take length of both
# ignore starting elements from the bigger list
# traverse together and find intersecting node
# ---------------------------------------------------------
# time = O(a+b)
# space = O(1)
# ---------------------------------------------------------

# helper
def addsamenode(lla, llb, value):
    node = c.Node(value)
    lla.tail.next = node
    lla.tail = node
    llb.tail.next = node
    llb.tail = node

def intersect(lla, llb):
    if lla.tail != llb.tail:
        return False
    lena = len(lla)
    lenb = len(llb)
    shorter = lla if lena < lenb else llb
    longer = llb if lena < lenb else lla
    diff = len(longer) - len(shorter)
    longernode = longer.head
    shorternode = shorter.head
    for i in range(diff):
        longernode = longernode.next
    while shorternode is not longernode:
        shorternode = shorternode.next
        longernode = longernode.next
    return longernode

ll1 = c.CustomLL()
for i in [3,1,5,9]:
    ll1.add(i)
ll2 = c.CustomLL()
for i in [2,4,6]:
    ll2.add(i)
for i in [7,2,1]:
    addsamenode(ll1, ll2, i)
print(ll1)
print(ll2)
print(intersect(ll1, ll2))
