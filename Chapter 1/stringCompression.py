# O(N)

def string_compression(string):
    # left pointer to know which position to update
    # the original array with the encoded contents.
    left = 0
    i = 0
    compressed = string.copy()

    while i < len(string):
        char = string[i]
        length = 1

        # check if i + 1 is valid and if the characters are a match
        while (i + 1) < len(string) and char == string[i + 1]:
            length += 1
            i += 1

        # keep original character
        compressed[left] = char
        # modify array in place if length of repeating char > 1
        if length > 1:
            len_str = str(length)
            compressed[left+1: left+1+len(len_str)] = len_str
            # increment left pointer according to the length of the encoded contents.
            left += len(len_str)
        elif length == 1:
            compressed[left + 1] = '1'
            left += 1
        left += 1
        i += 1
    return min(''.join(compressed[:left]), ''.join(string), key=len)

def teststring_compression():
    print('testing string_compression()...', end=" ")
    assert(string_compression(["a","a","b","b","c","c","c"]) == 'a2b2c3')
    assert(string_compression(["a","b","b","b","b","b","b","b","b","b","b","b","b"]) == 'a1b12')
    print('Passed!')

def main():
    teststring_compression()

if __name__ == '__main__':
    main()