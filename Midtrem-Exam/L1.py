# Level 1
import math
def all_equal_int(x1, x2, x3, x4):
    """Return True if all input integers, x1, x2, x3, and x4 are equal

    >>> all_equal_int(3, 3, 3, 3)
    True

    >>> all_equal_int(3, 2, 2, 3)
    False

    >>> all_equal_int(3, 2, 2, 2)
    False

    >>> all_equal_int(3, 3, 3, 2)
    False

    """
    if x1==x2 and x2==x3 and x3==x4:
        return True
    else:   return False

def circles_overlapping(x1, y1, x2, y2, r):
    """Return True if two circles with the same radius, r, located at (x1, y1) and (x2, y2) overlapped; return False, otherwise

    >>> circles_overlapping(0, 0, 2, 0, 2)
    True

    >>> circles_overlapping(2, 2, 4, 2, 0.7)
    False

    >>> circles_overlapping(1, 1, 2, 2, 0.6)
    False

    >>> circles_overlapping(1, 1, 4, 5, 3)
    True

    """
    # print(abs((x2-x1)**2 + (y2-y1)**2))
    # print((2*r)**2)
    if (abs((x2-x1)**2 + (y2-y1)**2) > (2*r)**2):
        return False
    else:   return True

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)