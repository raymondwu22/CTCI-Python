# O(N)

from LinkedList import LinkedList

def kthToLast(ll, k):
    current = ll.head
    length = 0

    # get the length of the LinkedList
    while current is not None:
        current = current.next
        length += 1

    if k > length:
        return

    # reset current pointer to the head
    current = ll.head
    for i in range(0, length - k):
        current = current.next

    return current.data

ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
print(kthToLast(ll, 3))