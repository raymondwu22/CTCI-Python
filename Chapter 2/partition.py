# [2.4] Partition: Write code to partition a linked list around
# a value x, such that all nodes less than x come before all
# nodes greater than or equal to x. If x is contained within
# the list, the values of x only need to be after the elements
# less than x (see below). The partition element x can appear
# anywhere in the "right partition"; it does not need to appear
# between left anr right partitions.

# EXAMPLE
# Input: 3, 5, 8, 5, 10, 2, 1 (partition = 5)
# Output: 3, 1, 2, 10, 5, 5, 8

# Space complexity: O(1)
# Time complexity: O(N)

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