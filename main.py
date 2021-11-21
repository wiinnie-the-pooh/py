import re
from typing import *
from collections import *
import math
import copy


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def list2nodes(numbers):
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def nodes2list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        t = n >> 1
        c = 0
        while t:
            t = t >> 1
            c += 1

        v = 1 << c
        res = (v == n)
        return res

assert Solution().isPowerOfTwo(n = 0) == False
assert Solution().isPowerOfTwo(n = 6) == False
assert Solution().isPowerOfTwo(n = 1) == True
assert Solution().isPowerOfTwo(n = 7) == False
assert Solution().isPowerOfTwo(n = 16) == True
