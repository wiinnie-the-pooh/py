#!/usr/bin/env pytest

from cmath import log10
import copy
import math
import re
from collections import *
from turtle import st
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
    def run(self, low: int, high: int) -> List[int]:
        digits = math.floor(math.log10(low))
        start = []
        tmp = low
        while tmp > 0:
            num = tmp % 10
            start.insert(0, num)
            tmp = int(tmp / 10)
            pass
        endi = len(start)
        start2 = copy.copy(start)

        def list2num(lst: List) -> int:
            num = lst[0]
            endi = len(lst)
            for i in range(1, endi):
                num = num * 10 + lst[i]
            return num

        res = []
        while True:
            start2 = [start2[0] + i for i in range(endi)]
            low2 = list2num(start2)
            if low2 > high:
                break
            if start2[0] + endi - 1 > 9:
                endi += 1
                start2 = [i + 1 for i in range(endi)]
                continue
            else:
                start2[0] += 1
            if low2 >= low:
                res.append(low2)
        return res

def test_current():
    assert Solution().run(low = 124, high = 300) == [234]
    assert Solution().run(low = 100, high = 300) == [123,234]
    assert Solution().run(low = 1000, high = 13000) == [1234,2345,3456,4567,5678,6789,12345]
    pass


def test_rest():
    pass
