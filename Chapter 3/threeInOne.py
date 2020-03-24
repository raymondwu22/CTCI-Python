# [3.1] Three in One: Describe how you could use a single
# array to implement three stacks.

# Approach 1: Fixed Division
# We can divide the array in three equal parts and allow the individual stack to grow in that limited space.
# Note: We will use the notation "[" to mean inclusive of an end point
# and "(" to mean exclusive of an end point.
# For stack 1, we will use [0,X).
# For stack 2, we will use [X,2X).
# For stack 3, we will use [2X,n).

import unittest

class MultiStack:
    def __init__(self, stackCapacity):
        self.numOfStacks = 3
        self.data = [0] * (stackCapacity * self.numOfStacks)
        self.sizes = [0] * self.numOfStacks
        self.stackCapacity = stackCapacity

    #  pop item from top of stack
    def pop(self, stackNum):
        if self.isEmpty(stackNum):
            raise Exception('Stack is Empty!')

        topIndex = self.indexOfTop(stackNum)
        value = self.data[topIndex]
        self.data[topIndex] = 0 # clear
        self.sizes[stackNum] -= 1
        return value

    # push values onto stack
    def push(self, item, stackNum):
        if self.isFull(stackNum):
            raise Exception('The stack is full!')
        self.sizes[stackNum] += 1
        self.data[self.indexOfTop(stackNum)] = item

    def peek(self, stackNum):
        if self.isEmpty(stackNum):
            raise Exception('Stack is Empty!')
        return self.data[self.indexOfTop(stackNum)]

    def isEmpty(self, stackNum):
        return self.sizes[stackNum] == 0

    def isFull(self, stackNum):
        return self.sizes[stackNum] == self.stackCapacity

    def indexOfTop(self, stackNum):
        offset = stackNum * self.stackCapacity
        size = self.sizes[stackNum]
        return offset + size - 1

class Test(unittest.TestCase):
    def testPush(self):
        s = MultiStack(5)
        s.push(3, 0)
        s.push(2, 1)
        s.push(5, 1)
        self.assertEqual(s.data[0], 3)
        self.assertEqual(s.data[5], 2)
        self.assertEqual(s.data[6], 5)

    def testPop(self):
        s = MultiStack(5)
        s.push(3, 0)
        s.push(2, 1)
        s.push(5, 1)
        self.assertEqual(s.pop(0), 3)
        self.assertEqual(s.pop(1), 5)
        self.assertEqual(s.pop(1), 2)
        self.assertRaises(Exception, s.pop, 1)

    def testPeek(self):
        s = MultiStack(5)
        s.push(3, 0)
        s.push(2, 1)
        s.push(5, 1)
        s.push(6, 2)
        self.assertEqual(s.peek(0), 3)
        self.assertEqual(s.peek(1), 5)
        self.assertEqual(s.peek(2), 6)

if __name__ == '__main__':
    unittest.main()