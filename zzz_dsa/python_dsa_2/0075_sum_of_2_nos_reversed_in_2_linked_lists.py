my = __import__("0071_custom_singly_linked_list")

def sumList(llA, llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = my.LinkedList()
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.add(int(result % 10))
        carry = result / 10
    if int(carry) != 0:
        ll.add(int(carry))
    return ll

llA = my.LinkedList()
llA.add(2)
llA.add(0)
llA.add(5)

llB = my.LinkedList()
llB.add(9)
llB.add(6)
llB.add(5)

print(llA)
print(llB)

print(sumList(llA, llB))
