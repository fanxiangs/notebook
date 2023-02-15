#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def insert_tail_without(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            node.next = self.head
            return node
        cur = self.head
        while cur:
            cur = cur.next
            if cur.next == self.head:
                cur.next = node
                node.next = self.head
                break

    def insert_heard_without(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            node.next = self.head
        cur = self.head
        while cur:
            cur = cur.next
            if cur.next == self.head:
                cur.next = node
                node.next = self.head
                self.head = node
                break

    def insert_without(self, index: int, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        pre_node = Node
        cur = self.head
        while index > 0:
            pre_node = cur
            cur = cur.next
            index -= 1
        node.next = cur
        pre_node.next = node

    def insert_head(self, data):
        node = Node(data)
        if self.head is None:
            node.next = self.head
            self.tail = self.head = node
        node.next = self.head
        self.tail = node

    def insert_tail(self, data):
        node = Node(data)
        if self.head is None:
            node.next = node
            self.head = self.tail = node
        cur = self.head
        if cur.next != self.head:
            cur = cur.next
        cur.next = node
        self.tail = node
        node.next = self.head


if __name__ == '__main__':
    cl = CircularLinkedList()
    # cl.insert_tail_without(1)
    # cl.insert_tail_without(2)
    # cl.insert_tail_without(3)
    # cl.insert_tail_without(4)
    cl.insert_tail(1)
    cl.insert_tail(2)
    cl.insert_tail(3)
    cl.insert_tail(4)
    cl.insert_tail(5)
    cl.insert_tail(6)
    cl.print_all()
