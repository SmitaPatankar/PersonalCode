my = __import__("0071_custom_singly_linked_list")

def nthToLast(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head

    for _ in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next

    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

customLL = my.LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print(nthToLast(customLL, 3))
