#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None

    def print_all(self):
        if self.head is None:
            return
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def insert_hard(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insert_tail(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = node
        node.prev = cur

    def insert(self, index, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        cur = self.head
        while index > 1:
            index -= 1
            cur = cur.next
        cur.prev.next = node
        node.next = cur
        node.prev = cur.prev
        cur.prev = node


if __name__ == '__main__':
    db_link = DoublyLinkedList()
    db_link.insert_hard(1)
    db_link.insert_hard(2)
    db_link.insert_hard(4)
    db_link.insert_tail(5)
    db_link.insert_tail(6)
    db_link.insert(2, 3)
    db_link.print_all()
