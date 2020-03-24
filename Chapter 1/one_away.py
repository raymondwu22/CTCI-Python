# [1:5]. One Away: There are three types of edits that can be
# performed on strings: insert a character, remove a character,
# or replace a character. Given two strings, write a function
# to check if they are one edit (or zero edits) away.

# Time complexity: O(n). Where n is the shorter string
# Space complexity: O(1). only creating pointers and a counter

import unittest

def one_away(str1, str2):
    char_set = [0 for _ in range(128)]

    for char in str1:
        val = ord(char)
        char_set[val] += 1

    for char in str2:
        val = ord(char)
        char_set[val] -= 1

    neg_count = pos_count = 0
    for item in char_set:
        if item > 0:
            pos_count += item
        elif item < 0:
            neg_count += item

    return neg_count > -2 and pos_count < 2

class Test(unittest.TestCase):
    def testOneAway(self):
        self.assertTrue(one_away('pale', 'ple'))
        self.assertTrue(one_away('pales', 'pale'))
        self.assertTrue(one_away('pale', 'bale'))
        self.assertFalse(one_away('pale', 'bake'))

if __name__ == '__main__':
    unittest.main()