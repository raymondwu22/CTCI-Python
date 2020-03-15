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

def testURLify():
    print('testing URLify()...', end=" ")
    assert(URLify('Mr John Smith    ', 13) == "Mr%20John%20Smith")
    assert (URLify('much ado about nothing      ', 22) == "much%20ado%20about%20nothing")
    print('Passed!')

def main():
    testURLify()

if __name__ == '__main__':
    main()