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
    def run(self, nums: List[int]) -> int:
        endi = len(nums)
        def step(cur: int, acc: int) -> int:
            if cur >= endi:
                return acc
            acc += nums[cur]
            ext = acc
            for i in range(cur + 2, endi):
                tmp = step(i, acc)
                ext = max(tmp, ext)
            acc = ext
            return acc

        res1 = step(0, 0)
        res2 = step(1, 0)
        res = max(res1, res2)
        return res

assert Solution().run(nums = [2,7,9,3,1]) == 12
assert Solution().run(nums = []) == 0
assert Solution().run(nums = [1]) == 1
assert Solution().run(nums = [1,0,0,1]) == 2
assert Solution().run(nums = [1,2,3,1]) == 4
