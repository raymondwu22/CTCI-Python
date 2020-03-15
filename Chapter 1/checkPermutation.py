#O(N)

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


def testcheck_permutation():
    print('testing check_permutation()...', end=" ")
    assert(checkPermutation('abcd', 'd2cba') == False)
    assert(checkPermutation('dcw4f', 'dcw5f') == False)
    assert(checkPermutation('abcd', 'd2cba') == False)
    print('Passed!')

def main():
    testcheck_permutation()

if __name__ == '__main__':
    main()