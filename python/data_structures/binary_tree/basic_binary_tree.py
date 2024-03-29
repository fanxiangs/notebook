# -*- coding: UTF-8 -*-
class Node:
    """节点类"""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    """树类"""

    def __init__(self, root=None):
        # 初始化树类，有一个根节点构成，开始为空
        self.root = root

    def add(self, elem):
        # 添加节点
        node = Node(elem)
        if self.root == Node:
            self.root = node
        else:
            queue = [self.root]
            # 对已有的队列进行遍历
            while queue:
                cur = queue.pop()
                if cur.left is None:
                    cur.left = node
                    return
                elif cur.right is None:
                    cur.right = node
                    return
                else:
                    # 如果左右子树都不为空加入队列继续判断
                    queue.append(cur.left)
                    queue.append(cur.right)


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
