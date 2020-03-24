# [2.6] Palindrome: Implement a function to check if
# a linked list is a palindrome.

# Time Complexity: O(N)
# Space Complexity: O(N)

from LinkedList import LinkedList
def palindrome(list):
    if not list:
        return None

    fast = slow = list.head
    stack = []

    # iterate to the middle of the list
    # build stack for comparison
    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next
    # odd lists
    if fast:
        slow = slow.next

    while slow:
        top = stack.pop()

        if top != slow.data:
            return False
        slow = slow.next

    return True

ll_true = LinkedList([1, 2, 3, 4, 5, 4, 3, 2, 1])
print(palindrome(ll_true))
ll_true1 = LinkedList([1, 2, 3, 4, 5, 5, 4, 3, 2, 1])
print(palindrome(ll_true1))
ll_false = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(palindrome(ll_false))