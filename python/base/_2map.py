# -*- coding: UTF-8 -*-
"""
@time:2020/04/12
"""
"""
map(func, *iterables) --> map object
"""
s = map(lambda x: x * 2, range(7))
for i in s:
    print(i)


def add(x):
    return x + 100


s = map(add, [1, 2, 3])
for i in s:
    print(i)

"""zip(*iterables) --> zip object"""
s = zip([1, 2, 3], [4, 5, 6])
for i in s:
    print(i)
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
xyz = zip(x, y, z)
print('---------')
for i in xyz:
    print(i)
print('---------')
xyz = zip(x, y, z)
u = zip(*xyz)
for i in u:
    print(i)
# 两个列表生成字典
a = ['a', 'b', 'c', 'd']
b = [1, 2, 3]
myDict = dict(zip(a, b))
print(myDict)
