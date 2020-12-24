# Level 3

def string_union(str1, str2):
    """Return a union of the characters in the two input strings str1 and str2; you can assume that the two strings have no duplicate characters

    >>> string_union("abcde", "abcwxyz")
    'abcdewxyz'

    >>> string_union("abcde", "wxyz")
    'abcdewxyz'

    >>> string_union("abcde", "wxyabzc")
    'abcdewxyz'

    """
    ans = ''
    for char in str1:
        ans += char
    # print(ans)
    for char in str2:
        if char not in ans:
            ans += char
    # print(ans)
    # return str1+str2
    return ans

def string_intersect(str1, str2):
    """Return an intersection of the characters in the two input strings str1 and str2; you can assume that the two strings have no duplicate characters

    >>> string_intersect("abcde", "abcwxyz")
    'abc'

    >>> string_intersect("abcde", "wxyz")
    ''

    >>> string_intersect("abcde", "wxyabzc")
    'abc'

    """
    ans = ''
    for char1 in str1:
        for char2 in str2:
            if char1 == char2:
                ans+= char1
    return ans

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)