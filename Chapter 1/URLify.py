# 1.3. URLify: Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold
# the additional characters, and that you are given the "true" length of
# the string.

# Input: "Mr John Smith", 13
# Output: "Mr%20John%20Smith"

# Time complexity: O(n) goes through each char in string
# Space complexity: O(n + 2k) creating new list and for each
#                   space will add two additional chars
#                   e.g. ' ' will become '%20'

import unittest

def URLify(string, length):
    string = string.strip()
    count_spaces = string.count(' ')
    newLength = length + 2 * count_spaces
    solution = [char for char in string] + [0] * count_spaces * 2

    for i in range(length - 1, 0, -1):
        if string[i] == ' ':
            solution[newLength - 3:newLength] = '%20'
            newLength -= 3
        else:
            solution[newLength - 1] = string[i]
            newLength -= 1

    return ''.join(solution)

class Test(unittest.TestCase):
    def test_url(self):
        self.assertEqual(URLify("Mr John Smith   ", 13), "Mr%20John%20Smith")
        self.assertEqual(URLify("he lloo", 7), "he%20lloo")
        self.assertEqual(URLify("he llo  ", 6), "he%20llo")

if __name__ == "__main__":
    unittest.main()