from collections import Counter
# O(N)
def check_permutation(s1, s2):
    if len(s1) != len(s2):
        return False

    counter = Counter()
    for char in s1:
        counter[char] += 1

    for char in s2:
        if counter[char] == 0:
            return False
        counter[char] -= 1

    return True


def testcheck_permutation():
    print('testing check_permutation()...', end=" ")
    assert(check_permutation('abcd', 'd2cba') == False)
    assert(check_permutation('dcw4f', 'dcw5f') == False)
    assert(check_permutation('abcd', 'd2cba') == False)
    print('Passed!')

def main():
    testcheck_permutation()

if __name__ == '__main__':
    main()