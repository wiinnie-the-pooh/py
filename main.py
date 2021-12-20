import copy
import math
import re
from collections import *
from typing import *


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


class Solution:
    def run(self, nums: List[int], k: int) -> int:
        wsum = sum(nums)
        endi = len(nums)
        lsum = {0: 0}
        rsum = {wsum: endi - 1}
        lcsum = 0
        rcsum = wsum
        for i, j in zip(range(endi), reversed(range(endi))):
            lcsum += nums[i]
            rcsum -= nums[j]
            if lcsum not in lsum:
                lsum[lcsum] = i + 1
            if rcsum not in rsum:
                rsum[rcsum] = j - 1
            pass

        assert rcsum == 0
        assert lcsum == wsum

        mdist = -math.inf
        for lval in sorted(lsum):
            i = lsum[lval]
            rval = lval + k
            if rval not in rsum:
                continue

            j = rsum[rval]
            dist = j - i + 1
            if dist < mdist:
                continue

            mdist = dist
            pass

        if mdist < 0:
            return 0

        return mdist


def test_current():
    assert Solution().run(nums=[-5, 8, 2, -1, 6, -3, 7, 1, 8, -2, 7], k=-4) == 0
    assert Solution().run(nums=[-1, 1], k=-1) == 1
    assert Solution().run(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4], k=0) == 4
    pass


def test_rest():
    assert Solution().run(nums=[1, -1, 5, -2, 3], k=3) == 4
    pass
