from collections import defaultdict
from typing import List
from collections import Counter
import cProfile
import cProfile, pstats, io
from pstats import SortKey


def profile(func):
    """Decorator for run function profile"""

    def wrapper(*args, **kwargs):
        profile_filename = func.__name__ + ".prof"
        profiler = cProfile.Profile()
        result = profiler.runcall(func, *args, **kwargs)
        s = io.StringIO()
        sortby = SortKey.CUMULATIVE
        ps = pstats.Stats(profiler, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        # profiler.dump_stats(profile_filename)
        return result

    return wrapper


class LinkedNode:
    def __init__(self, val, root_sorted, root_stack):
        self.value = val
        self.next_stack = root_stack
        if val is not None:
            cur_before, next_sorted = LinkedNode.sorted_before(root_sorted, val)
            self.next_sorted = next_sorted
            if cur_before is not None:
                cur_before.next_sorted = self
        else:
            self.next_sorted = None

    def __bool__(self):
        return self.value is not None

    @staticmethod
    def sorted_before(root, val):
        cur_before = None
        cur_after = root
        while cur_after:
            if cur_after.value <= val:
                break
            cur_before = cur_after
            cur_after = cur_after.next_sorted
        return cur_before, cur_after

    @staticmethod
    def remove(node, root_sorted, root_stack):
        before = None
        cur = root_sorted
        while cur is not node:
            before = cur
            cur = cur.next_sorted
        if before is not None:
            before.next_sorted = node.next_sorted
        else:
            root_sorted = node.next_sorted

        before = None
        cur = root_stack
        while cur is not node:
            before = cur
            cur = cur.next_stack
        if before is not None:
            before.next_stack = node.next_stack
        else:
            root_stack = node.next_stack

        return root_sorted, root_stack


root = end = LinkedNode(None, None, None)
assert not end
assert end.next_sorted is None

node01 = root_sorted = root_stack = LinkedNode(5, end, end)
assert node01.next_stack is end
assert node01.next_sorted is end

node02 = root_stack = LinkedNode(1, root_sorted, root_stack)
assert node01.next_stack is end
assert node01.next_sorted is node02

assert node02.next_stack is node01
assert node02.next_sorted is end

node03 = root_sorted = root_stack = LinkedNode(5, root_sorted, root_stack)
assert node01.next_stack is end
assert node01.next_sorted is node02

assert node02.next_stack is node01
assert node02.next_sorted is end

assert node03.next_stack is node02
assert node03.next_sorted is node01

assert LinkedNode.sorted_before(root, -1) == (None, end)

root = LinkedNode(1, root, root)
assert root.next_sorted == end
assert LinkedNode.sorted_before(root, 1) == (None, root)
assert LinkedNode.sorted_before(root, 3) == (None, root)

root2 = LinkedNode(3, root, root)
assert LinkedNode.sorted_before(root2, 3) == (None, root2)

node2 = LinkedNode(2, root2, root2)
assert node2.next_sorted == root
assert root2.next_sorted == node2


def gen_sorted(root):
    arr = []
    cur = root
    while cur:
        arr.append(cur.value)
        cur = cur.next_sorted
    return arr


assert gen_sorted(root2) == [3, 2, 1]


def gen_stack(root):
    arr = []
    cur = root
    while cur:
        arr.append(cur.value)
        cur = cur.next_stack
    return arr


assert gen_stack(node2) == [2, 3, 1]

root_sorted, root_stack = LinkedNode.remove(node2, root2, node2)
assert gen_sorted(root_sorted) == [3, 1]
assert gen_stack(root_stack) == [3, 1]

assert (root_sorted, root_stack) == (root2, root2)


class MaxStack:
    def __init__(self):
        self.root_stack = self.root_sorted = LinkedNode(None, None, None)

    def gen_sorted(self):
        return gen_sorted(self.root_sorted)

    def gen_stack(self):
        return gen_stack(self.root_stack)

    def push(self, x: int) -> None:
        self.root_stack = LinkedNode(x, self.root_sorted, self.root_stack)
        assert self.root_stack.value == x

        if not self.root_sorted or self.root_sorted.value <= x:
            self.root_sorted = self.root_stack

    def pop(self) -> int:
        res = self.root_stack.value
        self.root_sorted, self.root_stack = LinkedNode.remove(
            self.root_stack, self.root_sorted, self.root_stack
        )
        return res

    def top(self) -> int:
        return self.root_stack.value

    def peekMax(self) -> int:
        return self.root_sorted.value

    def popMax(self) -> int:
        res = self.root_sorted.value
        self.root_sorted, self.root_stack = LinkedNode.remove(
            self.root_sorted, self.root_sorted, self.root_stack
        )
        return res


cont = MaxStack()
cont.push(1)
assert cont.top() == 1
assert cont.peekMax() == 1

cont.push(3)
assert cont.top() == 3
assert cont.peekMax() == 3

cont.push(2)
assert cont.top() == 2
assert cont.peekMax() == 3

cont.popMax()
assert cont.top() == 2
assert cont.peekMax() == 2

cont.pop()
assert cont.top() == 1
assert cont.peekMax() == 1


cont = MaxStack()
cont.push(5)
cont.push(1)
cont.push(5)

assert cont.gen_stack() == [5, 1, 5]
assert cont.gen_sorted() == [5, 5, 1]

assert cont.top() == 5
cont.popMax()
assert cont.gen_sorted() == [5, 1]
assert cont.gen_stack() == [1, 5]

assert cont.top() == 1
assert cont.peekMax() == 5

assert cont.pop() == 1
assert cont.top() == 5