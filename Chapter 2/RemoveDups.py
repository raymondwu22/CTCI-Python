# O(N)
from LinkedList import LinkedList

def removeDups(linkedList):
    # empty
    if linkedList.head is None:
        return

    current = linkedList.head
    seen = {current.data}

    while current.next:
        if current.next.data not in seen:
            seen.add(current.next.data)
            current = current.next
        else:
            # already seen; delete pointer to that Node
            current.next = current.next.next

    return LinkedList

ll = LinkedList()
ll.generate(100, 0, 9)
print(ll)
removeDups(ll)
print(ll)