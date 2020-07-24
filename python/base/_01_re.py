# -*- coding: UTF-8 -*-
"""
@time:2020/04/11
"""
import re

"""
re.match(pattern, string, flags=0)
    从字符串的起始位置开始匹配,如果起始位置匹配不成功的话,就返回none
re.search(pattern, string, flags=0)
    扫描整个字符串并返回第一个成功的匹配
re.compile(pattern, flags=0)
    用于编译正则表达式,生成一个正则表达式Pattern对象,供 match() 和 search() 这两个函数使用
findall
    在字符串中找到正则表达式所匹配的所有子串,并返回一个列表,如果没有找到匹配的,则返回空列表
    注意： match 和 search 是匹配一次,而findall 是匹配所有
flags : 可选,表示匹配模式,比如忽略大小写,多行模式等,具体参数为：
re.I 忽略大小写
re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
re.M 多行模式
re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
re.X 为了增加可读性,忽略空格和 # 后面的注释
"""

line = "Cats are smarter 中文 than dogs"
r = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
print(r.groups())

r = re.match(r'(.*) are (.*?) ', line, re.M | re.I)
print(r.groups())
# print(r.group(1))
# print(r.group(2))
# r = re.search(r'(.*)', line)

str1 = 'hjggj小中文 明'.strip(' ')
print(str1)
pat = re.compile(r'[\u4e00-\u9fa5]+')
result = pat.findall(str1)
print(result)
r = re.search(r'[\u4e00-\u9fa5]+', str1)
print(r.group())

print('""".*?的理解"""')
""".*?的理解"""

s = '12><12>'
r = re.search(r'1.*?>', s)  # 12>
print(r.group())
r = re.search(r'1.*>', s)  # 12><12>
print(r.group())
