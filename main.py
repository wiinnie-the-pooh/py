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
        memo = dict()
        def step(cur: int) -> int:
            if cur >= endi:
                return 0

            if cur in memo:
                return memo[cur]

            acc = max(step(cur + 1), step(cur + 2) + nums[cur])
            memo[cur] = acc
            return acc

        res = step(0)
        return res

assert Solution().run(nums = [1,2,1,1]) == 3
assert Solution().run(nums = [2,7,9,3,1]) == 12
assert Solution().run(nums = []) == 0
assert Solution().run(nums = [1]) == 1
assert Solution().run(nums = [1,0,0,1]) == 2
assert Solution().run(nums = [1,2,3,1]) == 4
