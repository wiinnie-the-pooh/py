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
    def letterCasePermutation(self, s: str) -> List[str]:
        B = sum(letter.isalpha() for letter in s)
        ans = []

        lst = list(range(1 << B))
        for bits in lst:
            b = 0
            word = []
            for letter in s:
                if letter.isalpha():
                    if (bits >> b) & 1:
                        word.append(letter.lower())
                    else:
                        word.append(letter.upper())

                    b += 1
                else:
                    word.append(letter)

            ans.append("".join(word))
        return ans
assert Solution().letterCasePermutation(s = "a1b2") == ["a1b2","a1B2","A1b2","A1B2"]
assert Solution().letterCasePermutation(s = "12345") == ["12345"]
assert Solution().letterCasePermutation(s = "3z4") == ["3z4","3Z4"]
