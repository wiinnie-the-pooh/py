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
    def run(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i1 = m - 1
        i2 = n - 1
        i = len(nums1) - 1
        res = nums1
        while i1 != -1 and i2 != -1:
            if nums1[i1] > nums2[i2]:
                res[i] = nums1[i1]
                i1 -= 1
            else:
                res[i] = nums2[i2]
                i2 -= 1
            i -= 1
            pass
        if i2 != -1:
            while i != -1:
                res[i] = nums2[i2]
                i2 -= 1
                i -= 1
                pass

        return res

assert Solution().run(nums1 = [0], m = 0, nums2 = [1], n = 1) == [1]
assert Solution().run(nums1 = [1], m = 1, nums2 = [], n = 0) == [1]
assert Solution().run(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3) == [1,2,2,3,5,6]
