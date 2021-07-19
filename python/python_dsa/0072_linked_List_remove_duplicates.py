my = __import__("0071_custom_singly_linked_list")

def removeDups(ll):
    if ll.head is None:
        return
    else:
        currentNode = ll.head
        visited = set([currentNode.value])
        while currentNode.next:
            if currentNode.next.value in visited:
                currentNode.next = currentNode.next.next
            else:
                visited.add(currentNode.next.value)
                currentNode = currentNode.next
        return ll

customLL = my.LinkedList()
customLL.generate(99, 0, 99)
print(customLL)
print("###############")
removeDups(customLL)
print(customLL)
print("###############")
