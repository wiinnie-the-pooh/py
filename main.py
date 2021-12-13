import collections
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


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def tree2list(root):
    if not root:
        return []
    output = []
    queue = [root]
    current = 0
    lastval = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output.append(node)
            continue

        output.append(node.val)
        lastval = current
        queue.append(node.left)
        queue.append(node.right)

    return output[:lastval]


def list2tree(input):
    root = TreeNode(input[0])
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(input):
        node = nodeQueue[front]
        front = front + 1

        item = input[index]
        index = index + 1
        if item != None:
            leftNumber = item
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(input):
            break

        item = input[index]
        index = index + 1
        if item != None:
            rightNumber = item
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)

    return root


t = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
assert tree2list(list2tree(t)) == t

from collections import *


class Solution:
    def run2(self, nums: List[int]) -> List[int]:
        nums.sort()
        exp = 1
        res = []
        prev = None
        for i, val in enumerate(nums):
            if val == prev:
                continue
            prev = val
            if val != exp:
                res.append(exp)
            exp += 1
        res.extend((i for i in range(exp, len(nums) + 1)))
        return res

    def run(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        endi = len(nums)
        j = 0
        for i in range(1, endi + 1):
            while j != endi:
                val = nums[j]
                if val < i:
                    j += 1
                    continue
                if val == i:
                    j += 1
                    break
                res.append(i)
                break
        gen = [i for i in range(val + 1, endi + 1)]
        res.extend(gen)
        return res


def test_current():
    assert Solution().run(nums=[10, 2, 5, 10, 9, 1, 1, 4, 3, 7]) == [6, 8]


def test_rest():
    assert Solution().run(nums=[4, 3, 2, 7, 8, 2, 3, 1]) == [5, 6]
    assert Solution().run(nums=[1, 1]) == [2]
