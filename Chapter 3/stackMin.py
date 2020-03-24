# [3.2] Stack Min: How would you design a stack which,
# in addition to push and pop, has a function min which
# returns the minimum element? Push, pop, and min should
# all operate in O(1) time.

import unittest

class MultiStack:
    def __init__(self, stackSize):
        self.numStacks = 1
        self.array = [0] * (self.numStacks * stackSize)
        self.sizes = [0] * self.numStacks
        self.stackSize = stackSize
        self.minVals = 2**31

    def push(self, item, stackNum):
        if self.isFull(stackNum):
            raise Exception('Stack is full!')
        self.sizes[stackNum] += 1

        # if stack is empty, the min val is our new item
        if self.isEmpty(stackNum):
            self.minVals = item
        else:
        # else, take the min of the new item and our
        # previous min value
            self.minVals = min(item, self.minVals)
        # add the new item to our stack
        self.array[self.topIndex(stackNum)] = item


    def pop(self,stackNum):
        if self.isEmpty(stackNum):
            raise Exception('Stack is empty!')
        value = self.array[self.topIndex(stackNum)]

        if self.minVals == value:
            index = self.array.index(value)
            self.minVals = min(self.array[:index])

        self.array[self.topIndex(stackNum)] = 0 # set item to 0
        self.sizes[stackNum] -= 1
        return value

    def peek(self, stackNum):
        if self.isEmpty(stackNum):
            raise Exception('Stack is empty!')
        return self.array[self.topIndex(stackNum)]

    def min(self):
        return self.minVals

    def isEmpty(self, stackNum):
        return self.sizes[stackNum] == 0

    def isFull(self, stackNum):
        return self.sizes[stackNum] == self.stackSize

    def topIndex(self, stackNum):
        offset = stackNum * self.stackSize
        return offset + self.sizes[stackNum] - 1

class Test(unittest.TestCase):
    def testPush(self):
        s = MultiStack(10)
        s.push(2,0)
        s.push(3,0)
        s.push(1,0)
        self.assertEqual(s.array, [2, 3, 1, 0, 0, 0, 0, 0, 0, 0])

    def testPop(self):
        s = MultiStack(10)
        s.push(2,0)
        s.push(3,0)
        s.push(1,0)
        s.push(1,0)
        s.pop(0)
        s.pop(0)
        self.assertEqual(s.array, [2, 3, 0, 0, 0, 0, 0, 0, 0, 0])

    def testMin(self):
        s1 = MultiStack(10)
        s1.push(2,0)
        s1.push(3,0)
        s1.push(1,0)
        self.assertEqual(s1.min(), 1)

        s2 = MultiStack(10)
        s2.push(2,0)
        s2.push(5,0)
        s2.push(1,0)
        s2.push(1,0)
        s2.pop(0)
        s2.pop(0)
        self.assertEqual(s2.min(), 2)

if __name__ == '__main__':
    unittest.main()