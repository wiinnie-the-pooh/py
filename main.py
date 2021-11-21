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
    def run(self, n: int) -> int:
        c = p = n
        i = 0
        while p:
            c = p >> 1
            t = c << 1
            if t != p:
                i += 1
            p = c
        return i

assert Solution().run(n = 0b10000000) == 1

assert Solution().run(n = 0b1011) == 3
