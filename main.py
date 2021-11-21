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
    def climbStairs(self, n: int) -> int:
        arr = [0, 1, 2]
        if n < 3:
            return arr[n]
        res = -1
        for i in range(3, n + 1):
            res = arr[1] + arr[2]
            arr[1], arr[2] = arr[2], res
        
        return res


assert Solution().climbStairs(n = 3) == 3
assert Solution().climbStairs(n = 4) == 5
assert Solution().climbStairs(n = 2) == 2
