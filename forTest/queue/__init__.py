#!usr/bin/env python3
# -*- coding:utf-8 _*-
"""
@author:5uwst
@file:__init__.py.py
@time: 2019/7/19
"""

from forTest.array import Array
from forTest.linkedlist import LinkList


class Queue(object):
    """实现队列"""

    def __init__(self, queue, length=10):
        self._queue = queue
        self._length = length
        self._head = -1

    def is_empty(self):
        return self._head == -1

    def is_full(self):
        return self._head == self._length - 1

    def pop(self):
        if self.is_empty():
            raise RuntimeError("Queue is empty")
        item = self._queue.pop(0)
        self._head -= 1
        return item

    def push(self, item):
        if self.is_full():
            raise RuntimeError("Queue is full")
        self._queue.append(item)
        self._head += 1

    def __len__(self):
        return len(self._queue)

    def __contains__(self, item):
        return item in self._queue

    def __iter__(self):
        for d in self._queue:
            yield d

    def __str__(self):
        return "<{0}|{1}>".format(self.__class__.__name__, self._length)


class QueueByArray(Queue):
    """
    实现队列(By数组)
    """

    def __init__(self, length=10):
        super(QueueByArray, self).__init__(queue=Array(), length=length)


class QueueByLinkedList(Queue):
    """
    实现队列(By链表)
    """

    def __init__(self, length=10):
        super(QueueByLinkedList, self).__init__(queue=LinkList(), length=length)


def test_queue(queue_class):
    t = queue_class(length=6)
    print(t.is_empty())
    t.push(1)
    t.push(2)
    t.push(3)
    print(t.pop())
    t.push(4)
    print(t.pop())
    print(t.pop())
    # print(t.pop())
    print(t.is_full())
    print(len(t))
    for d in t:
        print(d)
    print(6 in t)


if __name__ == '__main__':
    cls = QueueByLinkedList
    test_queue(queue_class=cls)
