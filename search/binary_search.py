#!/usr/bin/env python

"""
    Binary Search
    -------------
    Recursively partitions the list until the `key` is found.
    Time Complexity:  O(lg n)
    Psuedo Code: http://en.wikipedia.org/wiki/Binary_search
"""


def search(seq, key):
    lo = 0
    hi = len(seq) - 1

    while hi >= lo:
        mid = lo + (hi - lo) // 2
        if seq[mid] < key:
            lo = mid + 1
        elif seq[mid] > key:
            hi = mid - 1
        else:
            return mid
    return False


test_list = [1, 6, 8, 9]
bsearch = search(test_list, 6)
print bsearch
