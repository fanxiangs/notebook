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
print("""filter(function or None, iterable) --> filter object""")


def is_odd(n):
    return n % 2 == 1


r = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(r))

l = [x for x in range(10)]
print(list(filter(lambda x: x % 2 == 1, l)))


def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    ftr = filter(_not_divisible(2), it)  # 1
    while True:
        n = next(ftr)  # 2
        yield n
        ftr = filter(_not_divisible(n), ftr)  # 3


for n in primes():
    if n < 100:
        print('now:', n)
    else:
        break
