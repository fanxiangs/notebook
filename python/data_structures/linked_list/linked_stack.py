#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack(object):
    def __init__(self):
        self.head = None
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

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise ValueError('stack is empty')
        res = self.head.data
        self.head = self.head.next
        self.size -= 1
        return res


if __name__ == '__main__':
    queue_stack = LinkedStack()
    queue_stack.push(1)
    queue_stack.push(2)
    queue_stack.push(3)
    queue_stack.print_all()
