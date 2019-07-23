#!usr/bin/env python3
# -*- coding:utf-8 _*-
"""
@author:5uwst
@file:__init__.py.py
@time: 2019/7/19
"""

from forTest.array import Array
from forTest.linkedlist import LinkList


class Stack(object):
    """
    实现栈
    """

    def __init__(self, length=10):
        self._length = length
        self._top = -1

    def is_empty(self):
        return self._top == -1

    def is_full(self):
        return self._top == self._length - 1

    def pop(self):
        raise NotImplementedError

    def push(self, item):
        raise NotImplementedError

    def __str__(self):
        return "<{0}|{1}>".format(self.__class__.__name__, self._length)


class StackByArray(Stack):
    """
    实现栈(By数组)
    """

    def __init__(self, length=10):
        super(StackByArray, self).__init__(length=length)
        self._stack = Array()

    def pop(self):
        if self.is_empty():
            raise RuntimeError("Stack is empty")
        data = self._stack.pop()
        self._top -= 1
        return data

    def push(self, item):
        if self.is_full():
            raise RuntimeError("Stack is full")
        self._stack.append(item)
        self._top += 1

    def __contains__(self, item):
        return item in self._stack

    def __iter__(self):
        for d in self._stack:
            yield d

    def __len__(self):
        return len(self._stack)


class StackByLinkedList(Stack):
    """
    实现栈(By链表)
    """

    def __init__(self, length=10):
        super(StackByLinkedList, self).__init__(length=length)
        self._stack = LinkList()

    def pop(self):
        if self.is_empty():
            raise RuntimeError("Stack is empty")
        self._top -= 1
        return self._stack.pop()

    def push(self, item):
        if self.is_full():
            raise RuntimeError("Stack is full")
        self._stack.append(item)
        self._top += 1

    def __len__(self):
        return len(self._stack)

    def __contains__(self, item):
        return item in self._stack

    def __iter__(self):
        for d in self._stack:
            yield d


def test_stack(stack_class):
    t = stack_class(6)
    print(t.is_full())
    print(t.is_empty())
    t.push(1)
    t.push(2)
    t.push(3)
    # t.pop()
    # t.pop()
    t.push(4)
    # t.pop()
    print(len(t))
    print(t.is_empty())
    for d in t:
        print(d)
    print(1 in t)


if __name__ == '__main__':
    cls = StackByLinkedList
    test_stack(stack_class=cls)

