# Level 4

def group_elements(l):
    """Return a list of lists where each list groups the same element(s) from the input list, l, together

    >>> group_elements([1, 3, 3, 4, 2, 5, 8, 5, 6, 7])
    [[1], [3, 3], [4], [2], [5, 5], [8], [6], [7]]

    >>> group_elements([3, 3, 3, 3])
    [[3, 3, 3, 3]]

    >>> group_elements([3, 3, 1, 3, 3, 1])
    [[3, 3, 3, 3], [1, 1]]

    >>> group_elements([5, 3, 1, 2, 4, 10])
    [[5], [3], [1], [2], [4], [10]]

    """
    ans =[]
    for i in l:
        if [i] not in ans:
            ans.append([i])
    
    for index,value in enumerate(l):
        for i in range(len(ans)):
            if value in ans[i]:
                ans[i].append(value)
    
    for index,value in enumerate(ans):
        ans[index].pop(0)
    return ans

def dup_elements(l):
    """Return a list that contains only duplicate elements of the input list, l; use the group_elements to help solve this one

    >>> dup_elements([1, 3, 3, 4, 2, 5, 8, 5, 6, 7])
    [3, 5]

    >>> dup_elements([3, 3, 3, 3])
    [3]

    >>> dup_elements([3, 3, 1, 3, 3, 1])
    [3, 1]

    >>> dup_elements([5, 3, 1, 2, 4, 10])
    []

    """
    ans = []
    for index1,value1 in enumerate(l):
        for index2,value2 in enumerate(l):
            if value1 == value2 and index1!=index2 and value1 not in ans:
                ans.append(value1)
    return ans

def count_unique_elements(l):
    """Return the total number of unique elements in the input list, l; use the group_elements to help solve this one

    >>> count_unique_elements([1, 3, 3, 4, 2, 5, 8, 5, 6, 7])
    6

    >>> count_unique_elements([3, 3, 3, 3])
    0

    >>> count_unique_elements([3, 3, 1, 3, 3, 1])
    0

    >>> count_unique_elements([5, 3, 1, 2, 4, 10])
    6

    """
    ans = len(l)
    lis = []
    for index1,value1 in enumerate(l):
        for index2,value2 in enumerate(l):
            if value1 == value2 and index1!=index2:
                # print(index1,value1 , index2,value2 , ans-1)
                # ans -= 1
                # pass
                try:
                    value1 == value2 and index1!=index2
                    ans -= 1
                    break
                except:
                    pass
    # for i in l:
    #     lis.append(i)
    # lis.sort()
    # lis = set(lis)
    # print(lis)
    # ans = len(lis)
    return ans

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)