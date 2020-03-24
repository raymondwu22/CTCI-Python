# [2.5] Sum Lists: You have two numbers represented by a linked
# list, where each node contains a single digit. The digits
# are stored in reverse order, such that the 1's digit is at
# the head of the list. Write a function that adds the two
# numbers and returns the sum as a linked list.

# Example: (7, 1, 6) + (5, 9, 2) -> (2,1,9)

# Space complexity: O(N)
# Time complexity: O(N)

from LinkedList import LinkedList

def sumLists(list1, list2):
    p1 = list1.head
    p2 = list2.head
    solution = LinkedList()
    carry = 0

    while p1 or p2:
        # carry from the previous loop is 'carried' over
        # to the result of the current loop
        result = carry
        if p1:
            result += p1.data
            p1 = p1.next
        if p2:
            result += p2.data
            p2 = p2.next
        solution.add(result % 10)
        carry = result // 10

    if carry:
        solution.add(carry)

    return solution

ll_a = LinkedList()
ll_a.generate(4, 0, 9)
ll_b = LinkedList()
ll_b.generate(3, 0, 9)
print(ll_a)
print(ll_b)
print(sumLists(ll_a, ll_b))
