# Time complexity: O(n + m), must go through all characters for both strings
# Space complexity: O(c), hash table will be size of available chars

import unittest

def checkPermutation(str1, str2):
    if len(str1) != len(str2):
        return False

    char_set = [0 for _ in range(128)]

    for char in str1:
        val = ord(char)
        char_set[val] += 1

    for char in str2:
        val = ord(char)
        if char_set[val] == 0:
            return False
        char_set[val] -= 1

    print(char_set)

    return True

class Test(unittest.TestCase):
    def testPermutation(self):
        self.assertTrue(checkPermutation('abcde','edcba'))
        self.assertFalse(checkPermutation('abcd', 'd2cba'))
        self.assertFalse(checkPermutation('dcw4f', 'dcw5f'))
        self.assertFalse(checkPermutation('abcd', 'd2cba'))

if __name__ == '__main__':
    unittest.main()