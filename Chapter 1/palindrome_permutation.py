# 1.4. Palindrome Permutation: Given a string, write a function to check
# if it is a permutation of a palindrome. A palindrome is a word or
# phrase that is the same forwards and backwards. A permutation is a
# rearrangement of letters. The palindrome does not need to be limited
# to just dictionary words.

# Input: Tact Coa
# Output: True

# Hash Table Solution
# Time complexity: O(n) count characters and then loop through smaller
# subset
# Space complexity: O(c) where c is each char / Also can be thought
# of as O(1) because set of characters is limited

import unittest

def palindrome_permutation(phrase):
    char_set = [0 for _ in range(128)]
    phrase = phrase.replace(" ", "").lower()

    for char in phrase:
        val = ord(char)
        char_set[val] += 1

    # Iterate through the hash table to make sure character counts
    # are all even or at most one value is odd.
    odd_count = 0

    for i in range(len(char_set)):
        if odd_count <= 1:
            odd_count += char_set[i] % 2

    return odd_count <= 1

class Test(unittest.TestCase):
    def testpalindrome_permutation(self):
        self.assertTrue(palindrome_permutation("Taco cat"))
        self.assertTrue(palindrome_permutation('jhsabckuj ahjsbckj'))
        self.assertFalse(palindrome_permutation('Random Words'))
        self.assertFalse(palindrome_permutation('Not a Palindrome'))

if __name__ == '__main__':
    unittest.main()
