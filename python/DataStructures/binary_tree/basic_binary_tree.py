# -*- coding: UTF-8 -*-
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def display(tree):
    if tree is None:
        return
    if tree.left is not None:
        display(tree.left)
    print(tree.data)
    if tree.right is not None:
        display(tree.right)
    return


def depth_of_tree(tree):
    if tree is None:
        return 0
    else:
        left_height = depth_of_tree(tree.left)
        right_height = depth_of_tree(tree.right)
        return max(left_height, right_height) + 1


def main():
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    tree.right.left = Node(6)
    tree.right.right = Node(7)
    tree.right.left.left = Node(8)
    tree.right.left.left.right = Node(9)
    r = depth_of_tree(tree)
    print(r)


if __name__ == '__main__':
    main()
