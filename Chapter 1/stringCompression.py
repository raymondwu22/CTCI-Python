# [1:6]. String Compression: Implement a method to perform basic string
# compression using the counts of repeated characters. For example,
# the string aabcccccaaa would become a2b1c5a3. If the "compressed"
# string would not become smaller than the original string, your method
# should return the original string. You can assume the string has only
# uppercase and lowercase letters (a-z)

# Time complexity: O(n)
# Space complexity: O(c) for distinct chars

import unittest

def stringCompression(string):
    if not string:
        return None
    if len(string) < 3:
        return string

    # pointer to know which position to update
    # the original array with the encoded contents.
    i = 0
    solution = []

    while i + 1 < len(string):
        char = string[i]
        length = 1
        # check if i + 1 is valid and if the characters are a match
        while i + 1 < len(string) and char == string[i + 1]:
            length += 1
            i += 1
        i += 1
        solution.append(char)
        solution.append(str(length))

    return min(''.join(solution), string, key=len)

class Test(unittest.TestCase):
    def teststring_compression(self):
        self.assertEqual(stringCompression(["a","a","b","b","c","c","c"]), 'a2b2c3')
        self.assertEqual(stringCompression(["a","b","b","b","b","b","b","b","b","b","b","b","b"]), 'a1b12')
        self.assertEqual(stringCompression('aaabbb'), 'a3b3')
        self.assertEqual(stringCompression('aaaaccccbaa'), 'a4c4b1a2')
        self.assertEqual(stringCompression('ababa'), 'ababa')

if __name__ == '__main__':
    unittest.main()