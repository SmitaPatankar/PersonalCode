my = __import__("0071_custom_singly_linked_list")

def partition(ll, x):
    curNode = ll.head
    ll.tail = ll.head

    while curNode:
        nextNode = curNode.next
        curNode.next = None
        if curNode.value < x:
            curNode.next = ll.head
            ll.head = curNode
        else:
            ll.tail.next = curNode
            ll.tail = curNode
        curNode = nextNode
    
    if ll.tail.next is not None:
        ll.tail.next = None

customLL = my.LinkedList()
customLL.generate(10,0,99)
print(customLL)
partition(customLL, 30)
print(customLL)
