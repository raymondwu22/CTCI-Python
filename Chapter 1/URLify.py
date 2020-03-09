# def URLify(s, length):
#     return s[:length].replace(' ', '%20')


def URLify(s, length):
    string = s.strip() # remove leading and trailing spaces
    solution = list(string)
    numOfSpaces = string.count(' ')

    # for every space, need two additional chars to accomodate '%20'
    new_length = length + numOfSpaces * 2

    for f in range(length, new_length):
        solution.append('0')

    # track index of solution
    index = new_length

    # start filling character from the end
    for j in reversed(range(length)):
        # # replace spaces
        if string[j] == ' ':
            solution[index-3: index] = '%20'
            index -= 3
        else:
            # move our characters
            solution[index - 1] = solution[j]
            index -= 1
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