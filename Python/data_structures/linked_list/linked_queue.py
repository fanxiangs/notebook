#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def print_all(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def enqueue(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError('stack is empty')
        res = self.head.data
        self.head = self.head.next
        self.size -= 1
        return res


if __name__ == '__main__':
    link_stack = LinkedQueue()
    link_stack.enqueue(1)
    link_stack.enqueue(2)
    link_stack.enqueue(3)
    link_stack.print_all()
    link_stack.dequeue()
    link_stack.print_all()
