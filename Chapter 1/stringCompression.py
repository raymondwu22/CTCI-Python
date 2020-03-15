def stringCompression(string):
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

def teststring_compression():
    print('testing string_compression()...', end=" ")
    assert(stringCompression(["a","a","b","b","c","c","c"]) == 'a2b2c3')
    assert(stringCompression(["a","b","b","b","b","b","b","b","b","b","b","b","b"]) == 'a1b12')
    print('Passed!')

def main():
    teststring_compression()

if __name__ == '__main__':
    main()