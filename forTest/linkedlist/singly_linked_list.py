#!usr/bin/env python3
# -*- coding:utf-8 _*-
"""
@author:5uwst
@file:singly_linked_list.py
@time: 2019/7/18
"""


class Node(object):
    """
    链表节点
    """

    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return "<{0}|{1}>".format(self.__class__.__name__, self.value)


class LinkList(object):
    """
    链表
    """

    def __init__(self):
        self._head = None
        self._length = 0

    def is_empty(self):
        """
        判断链表是否为空
        :return: bool
        """
        return self._length <= 0

    def append(self, item):
        """
        在尾部添加一个节点
        :param item:
        :return: None
        """
        new_node = self.__format(item)
        if not self._head:
            self._head = new_node
        else:
            node = self._head
            while node.next_node:
                node = node.next_node
            node.next_node = new_node
        self._length += 1

    def __bool__(self):
        return self.is_empty()

    def __iter__(self):
        return self.__get_value()

    def __len__(self):
        return self._length

    def __contains__(self, item):
        for v in self:
            if v == item:
                return True
        return False

    def __get_value(self):
        nt = self._head
        while nt:
            yield nt.value
            nt = nt.next_node

    def __get_node(self):
        nt = self._head
        while nt:
            yield nt
            nt = nt.next_node

    @staticmethod
    def __format(item):
        return Node(item) if not isinstance(item, Node) else item

    def __validate(self, index):
        if index > self._length - 1 or index < 0:
            raise SyntaxError

    def insert(self, item, index=0):
        """
        插入一个节点
        :param item:
        :param index:
        :return:
        """
        if self.is_empty():
            self.append(item)
            return
        self.__validate(index=index)
        new_node = self.__format(item)
        if index == 0:
            new_node.next_node = self._head
            self._head = new_node
            self._length += 1
            return
        i = 0
        nt = self._head
        pre = self._head
        while nt.next_node and i < index:
            pre = nt
            nt = nt.next_node
            i += 1
        new_node.next_node = nt
        pre.next_node = new_node
        self._length += 1

    def clear(self):
        self._head = Node
        self._length = 0

    def __find_value_by_index(self, index):
        self.__validate(index=index)
        for i, v in enumerate(self):
            if i == index:
                return v

    def __getitem__(self, item):
        return self.__find_value_by_index(index=item)

    def __setitem__(self, key, value):
        self.insert(value, index=key)

    def find(self, value):
        for i, v in enumerate(self):
            if v == value:
                return i
        else:
            return -1

    def update(self, index, value):
        self.__validate(index=index)
        for i, node in enumerate(self.__get_node()):
            if index == i:
                node.value = value

    def pop(self, index=None):
        if self.is_empty():
            raise SyntaxError
        index = self._length - 1 if index is None else index
        self.__validate(index=index)
        for i, node in enumerate(self.__get_node()):
            if i == index - 1:
                _next = node.next_node
                value = _next.value
                if index == self._length - 1:
                    node.next_node = None
                else:
                    node.next_node = _next.next_node
                self._length -= 1
                return value

    def remove(self, item):
        """
        删除一个节点
        :param item:
        :return:
        """
        if self.is_empty():
            raise SyntaxError
        if self._head.value == item:
            _next = self._head.next_node
            self._head = _next
            self._length -= 1
            return
        for i, node in enumerate(self.__get_node()):
            _next = node.next_node
            if _next and _next.value == item:
                if i == self._length - 2:
                    node.next_node = None
                else:
                    node.next_node = _next.next_node
                self._length -= 1
                return
        else:
            raise SyntaxError("{0} not in {1}".format(item, self.__class__.__name__))

    def __str__(self):
        return str([i for i in self])

    def __repr__(self):
        return "<{0}|{1}>".format(self.__class__.__name__, self._length)


def test_node():
    n1 = Node(1)
    n2 = Node(2)
    print(n1, n2, sep=", ")


def test_link():
    t = LinkList()
    print(t.is_empty())
    for i in range(4):
        t.append(i)
    print(len(t))
    print(t.is_empty())
    for v in t:
        print(v)
    print(11 in t)
    t.insert(55, 0)
    print(t)
    t.insert(44, 1)
    print(t)
    t.insert(33, 5)
    print(t)
    print(t[1])
    print(t.find(5))
    t.update(6, 90)
    print(t)
    print(list(t))
    t.pop()
    print(t)
    t.pop(2)
    print(t)
    t.remove(55)
    print(t)
    t.remove(666666)


if __name__ == '__main__':
    # test_node()
    test_link()
