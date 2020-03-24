# [3.3] Stack of Plates: Imagine a stack of plates. If the stack
# gets too high, it might topple. Therefore, in real life, we
# would literally start a new stack when the previous stack
# exceeds some threshold. Implement a data structure SetOfStacks
# that mimics this. SetOfStacks should be composed of several
# stacks and should create a new stack once the previous one
# exceeds capacity. SetOfStacks.push() and SetOfStacks.pop()
# should behave identically to a single stack (that is, pop()
# should return the same values as it would if there were just
# a single stack).

# FOLLOW UP: Implement a function popAt(index) which performs
# a pop operation on a specific sub-stack

import unittest

class SetOfStacks:
    def __init__(self, capacity):
        self.stacks = [[]]
        self.capacity = capacity

    def push(self, value):
        if len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])

        self.stacks[-1].append(value)

    def pop(self):
        # Ensure the last stack is not empty and more than one set of stacks
        if not self.stacks[-1] and len(self.stacks) == 1:
            raise IndexError('Cannot perform pop on an empty stack')

        value = self.stacks[-1].pop()
        self._clean_empty_list()

        return value

    def popAt(self,index):
        if index >= self.stack_length:
            raise IndexError('Pop index out of range')

        active_stack = index // self.capacity
        stack_index = index % self.capacity
        value = self.stacks[active_stack].pop(stack_index)

        self._clean_empty_list()

        # fill in the open spot in the stack
        if active_stack < len(self.stacks) - 1:
            time_carry = len(self.stacks) - active_stack - 1

            for i in range(time_carry):
                self.stacks[active_stack + i].\
                    append(self.stacks[active_stack + i + 1].pop(0))

        return value

    def _clean_empty_list(self):
        # if the last stack is empty, more than one set of stacks
        if not self.stacks[-1] and len(self.stacks) > 1:
            self.stacks.pop()

    @property
    def stack_length(self):
        last_stack_length = len(self.stacks[-1])
        remaining_length = self.capacity*(len(self.stacks) - 1)
        return last_stack_length + remaining_length

class Test(unittest.TestCase):
    def testPush(self):
        s = SetOfStacks(5)
        for i in range(1, 7):
            s.push(i)
        self.assertEqual(s.stacks, [[1, 2, 3, 4, 5], [6]])

    def testPop(self):
        s = SetOfStacks(5)
        for i in range(1, 7):
            s.push(i)
        popped_value = s.pop()
        self.assertEqual(popped_value, 6)
        self.assertEqual(s.stacks, [[1, 2, 3, 4, 5]])
        for i in range(5):
            s.pop()
        self.assertEqual(s.stacks, [[]])
        self.assertRaises(IndexError, s.pop)

    def testStackLength(self):
        s = SetOfStacks(5)
        s.stacks = [[1, 2, 3, 4, 5], [6, 7, 8]]
        self.assertEqual(s.stack_length, 8)

    def testPopAt(self):
        s = SetOfStacks(5)
        s.stacks = [[1, 2, 3, 4, 5], [6, 7, 8]]
        s.popAt(0)
        self.assertEqual(s.stacks, [[2, 3, 4, 5, 6], [7, 8]])
        s.popAt(3)
        self.assertEqual(s.stacks, [[2, 3, 4, 6, 7], [8]])
        s.popAt(5)
        self.assertEqual(s.stacks, [[2, 3, 4, 6, 7]])
        self.assertRaises(IndexError, s.popAt, 5)

if __name__ == '__main__':
    unittest.main()