#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: fan
# time: 11/06/2021

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

    def __repr__(self) -> str:
        """
        Get the string representation of this node.
        >>> Node(10).__repr__()
        'Node(10)'
        """
        return f"Node({self.data})"


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        cur = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def append(self, data):
        if data is None:
            return None
        node = Node(data)
        if self.head is None:
            self.head = node
            return node
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = node
        return node

    def add_first(self, data):
        if data is None:
            return None
        node = Node(data)
        node.next = self.head
        self.head = node
        return node

    def insert(self, index, data):
        if data is None:
            return None
        if index <= 0:
            self.add_first(data)
        elif index >= self.__len__():
            self.append(data)
        else:
            node = Node(data)
            cur = self.head
            while index > 1:
                cur = cur.next
                index -= 1
            target_node = cur.next
            cur.next = node
            node.next = target_node
            return node

    def print_link(self):
        cur = self.head
        while cur is not None:
            print(cur.data, end=',')
            cur = cur.next
        print(end='\n')

    def delete(self, data):
        if (data or self.head) is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        pre_node = None
        cur_node = self.head
        while cur_node.data != data and cur_node.next is not None:
            pre_node = cur_node
            cur_node = cur_node.next
        pre_node.next = cur_node.next

    def get_all_data(self):
        res = []
        cur_node = self.head
        while cur_node is not None:
            res.append(cur_node.data)
            cur_node = cur_node.next
        return res

    def reverse(self):
        if self.head is None:
            return
        pre_node = None
        cur_node = self.head
        while cur_node is not None:
            next_node = cur_node.next
            cur_node.next = pre_node
            pre_node = cur_node
            cur_node = next_node
        self.head = pre_node


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append(10)
    linked_list.append(11)
    linked_list.append(12)
    linked_list.print_link()
    linked_list.reverse()
    linked_list.print_link()
    r = Node(10)
    print(r)
