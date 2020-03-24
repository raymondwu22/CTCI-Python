# [2.3] Delete Middle Node: Implement an algorithm to delete a
# node in the middle (i.e., any node but the first and last
# node, not necessarily the exact middle) of a singly linked
# list, given only access to that node.

# Space complexity: O(1)
# Time complexity: O(N)

from LinkedList import LinkedList

def deleteNode(ll, node):
    current = ll.head
    runner = ll.head.next

    while runner.next:
        if runner == node:
            current.next = current.next.next
            return ll

        runner = runner.next
        current = current.next

    return None

# def deleteNode(node):
# #     node.data = node.next.data
# #     node.next = node.next.next

ll = LinkedList()
ll.add_multiple([1, 2, 3, 4])
middle_node = ll.add(5)
ll.add_multiple([7, 8, 9])

print(ll)
deleteNode(ll, middle_node)
# deleteNode(middle_node)
print(ll)