# Time complexity: O(n) because needs to check each character
# Space complexity: O(c) where c is each character

import unittest

def normalize(s):
    normalized = s.replace(" ", "")
    return normalized.lower()

# implementation with dictionary
# O(N)
def isUniqueDict(s):
    d = dict()
    temp = normalize(s)
    for char in temp:
        if char in d:
            return False
        d[char] = d.get(char, 0) + 1
    return True

# implementation with sets
# O(N)
def isUniqueSet(s):
    return len(set(s)) == len(s)

# implementation with hash table
# O(N)
def isUniqueHash(s):
    if len(s) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in s:
        val = ord(char)
        # char already exists
        if char_set[val]:
            return False
        char_set[val] = True

    return True

string1 = "noT rEady"
string2 = "StrInG RepeAtEd"
string3 = 'aabcdefg'

class Test(unittest.TestCase):
    def testUnique(self):
        self.assertTrue(isUniqueDict(string1))
        self.assertTrue(isUniqueHash(string1))
        self.assertTrue(isUniqueSet(string1))
        self.assertFalse(isUniqueDict(string2))
        self.assertFalse(isUniqueHash(string2))
        self.assertFalse(isUniqueSet(string2))
        self.assertFalse(isUniqueDict(string3))
        self.assertFalse(isUniqueHash(string3))
        self.assertFalse(isUniqueSet(string3))

if __name__ == '__main__':
    unittest.main()
