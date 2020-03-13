def palindrom_permutation(phrase):
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


def testpalindrom_permutation():
    print('testing palindrom_permutation()...', end=" ")
    assert(palindrom_permutation("Taco cat") == True)
    assert(palindrom_permutation('jhsabckuj ahjsbckj') == True)
    assert (palindrom_permutation('Random Words') == False)
    assert (palindrom_permutation('Not a Palindrome') == False)
    print('Passed!')

def main():
    testpalindrom_permutation()


if __name__ == '__main__':
    main()
