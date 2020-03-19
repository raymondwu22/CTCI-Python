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