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
    def run(self, triangle: List[List[int]]) -> int:
        endi = len(triangle)
        def step(i: int, j: int) -> int:
            ii = i + 1
            acc = triangle[i][j]
            if ii == endi:
                return acc
            acc1 = step(ii, j)
            acc2 = step(ii, j + 1)
            acc += min(acc1, acc2)
            return acc
        
        res = step(0, 0)
        return res

assert Solution().run(triangle = [[-10]]) == -10
assert Solution().run(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]) == 11
