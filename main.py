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
        r = 0
        for i in range(32):
            c = p >> 1
            t = c << 1
            r <<= 1
            if t != p:
                r += 1
                pass
            p = c
            # fmt = bin(r)
            pass
        return r

assert Solution().run(n = 0b11111111111111111111111111111101) == 0b10111111111111111111111111111111
assert Solution().run(n = 0b00000010100101000001111010011100) == 0b00111001011110000010100101000000
