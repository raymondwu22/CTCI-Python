# [2.8] Loop Detection: Given a circular linked list, implement
# an algorithm that returns the node at the beginning of the
# loop.

# Space complexity: O(1)
# Time complexity: O(n)

from LinkedList import LinkedList

# Floyd's cycle finding algorithm
def loopDetection(list):
    fast = slow = list.head

    while slow and fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            return True

    return False