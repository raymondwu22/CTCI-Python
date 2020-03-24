# [1.9] Assume you have a method isSubstring which checks
# if one word is substring of another. Given two strings,
# s1 and s2, write code to check if s2 is a rotation of s1
# using only one call to isSubstring (e.g., "waterbottle" is
# a rotation of "erbottlewat").

# Time complexity: O(N)

import unittest

def string_rotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return isSubstring(s1 + s2, s2)
    return False

def isSubstring(string, sub):
    return string.find(sub) != -1

class Test(unittest.TestCase):
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = string_rotation(s1, s2)
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()