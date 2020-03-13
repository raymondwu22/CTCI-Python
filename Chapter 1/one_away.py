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
        else:
            neg_count += item

    return neg_count > -2 and pos_count < 2

def testone_away():
    print('testing one_away()...', end=" ")
    assert(one_away('pale', 'ple') == True)
    assert(one_away('pales', 'pale') == True)
    assert(one_away('pale', 'bale') == True)
    assert(one_away('pale', 'bake') == False)
    print('Passed!')

def main():
    testone_away()


if __name__ == '__main__':
    main()