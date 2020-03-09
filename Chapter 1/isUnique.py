string1 = "noT rEady"
string2 = "StrInG RepeAtEd"

def normalize(s):
    normalized = s.replace(" ", "")
    return normalized.lower()

# implementation with dictionary
# O(N)
def isUniqueDict(s):
    d = dict()
    temp = normalize(s)
    for char in temp:
        if char in d:
            return False
        d[char] = d.get(char, 0) + 1
    return True

# implementation with sets
# O(N)
def isUniqueSet(s):
    return len(set(s)) == len(s)

# implementation with hash table
# O(N)
def isUniqueHash(s):
    if len(s) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in s:
        val = ord(char)
        # char already exists
        if char_set[val]:
            return False
        char_set[val] = True

    return True


def testIsUniqueDict():
    print('testing isUniqueDict()...', end=" ")
    assert(isUniqueDict(string1) == True)
    assert(isUniqueDict(string2) == False)
    print('Passed!')

def testIsUniqueSet():
    print('testing isUniqueSet()...', end=" ")
    assert (isUniqueSet(string1) == True)
    assert (isUniqueSet(string2) == False)
    print('Passed!')

def testIsUniqueHash():
    print('testing isUniqueHash()...', end=" ")
    assert(isUniqueHash(string1) == True)
    assert(isUniqueHash(string2) == False)
    print('Passed!')

def main():
    testIsUniqueDict()
    testIsUniqueSet()
    testIsUniqueHash()

if __name__ == '__main__':
    main()
