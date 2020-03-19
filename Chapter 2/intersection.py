# O(N+M)
from LinkedList import LinkedList

def intersection(list1, list2):
    if list1.tail is not list2.tail:
        return False

    shorter = list1 if len(list1) < len(list2) else list2
    longer = list1 if len(list1) > len(list2) else list2

    shorter_node = shorter.head
    longer_node = longer.head

    # get the difference of counts
    diff = len(longer) - len(shorter)

    # traverse the bigger list from the first node till d nodes.
    # both the lists will have equal number of nodes.
    for i in range(diff):
        longer_node = longer_node.next

    # traverse both lists in parallel to find the intersecting node
    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    return longer_node