from LinkedList import LinkedList

def partition(ll, val):
    current = ll.tail = ll.head

    while current:
        # temporary pointer to next node
        next = current.next

        # move to the left of our partition
        if current.data < val:
            current.next = ll.head
            ll.head = current
        else:
            # set new tail
            ll.tail.next = current
            ll.tail = current
            current.next = None
        current = next

        if ll.tail.next is not None:
            ll.tail.next = None

ll = LinkedList()
ll.generate(10, 0, 50)
print(ll, 'head:', ll.head.data)
partition(ll, ll.head.data)
print(ll)