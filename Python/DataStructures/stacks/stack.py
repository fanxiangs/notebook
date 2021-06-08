#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: fan
# time: 06/07/2021

class StackOverflowError(Exception):
    pass


class Stack:
    def __init__(self, limit=10):
        self.items = []
        self.limit = limit

    def __str__(self):
        return str(self.items)

    def push(self, val):
        if self.size() >= self.limit:
            raise StackOverflowError
        self.items.append(val)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]

    def __contains__(self, item) -> bool:
        """Check if item is in stack"""
        return item in self.items


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    print(s)
    s.push(2)
    s.push(2)
    print(s)
    print(s.size())
    print(s.pop())
    assert 2 in s
    assert s.peek() == 2
