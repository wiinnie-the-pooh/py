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
    def run(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        if last == 0:
            return True
        stack = set()
        idx = 0
        while True:
            addons = [idx + i for i in range(1, nums[idx] + 1) if i + idx <= last]
            stack |= set(addons)
            if not stack:
                return False
            if last in stack:
                return True
            idx = stack.pop()
        return False


def test_current():
    assert Solution().run(nums=[1, 2]) == True
    pass


def test_rest():
    assert Solution().run(nums=[0]) == True
    assert Solution().run(nums=[1]) == True
    assert Solution().run(nums=[2, 3, 1, 1, 4]) == True
    assert Solution().run(nums=[3, 2, 1, 0, 4]) == False
    pass
