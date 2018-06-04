# -*- coding: UTF-8 -*-
'''
re 模块有两种方式：

#将正则表达式编译成一个Pattern规则对象

    re.compile(pattern[, flags])
    作用：把正则表达式语法转化成正则表达式对象
    flags定义包括：
    re.I：忽略大小写
    re.L：表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
    re.M：多行模式
    re.S：’ . ’并且包括换行符在内的任意字符（注意：’ . ’不包括换行符）
    re.U： 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库

pattern = re.compile("\d")

match(str, begin, end)
pattern.match("123") #从起始位置往后查找，返回第一个符合规则的，只匹配一次

search(str, begin, end)
pattern.search()#从任何位置开始往后查找，返回第一个符合规则的，只匹配一次

pattern.findall()#所有的全部匹配，返回列表

pattern.finditer()#所有的全部匹配，返回的使是一个迭代器

pattern.split()#分割字符串，返回列表

pattern.sub()#替换

match(str, begin, end)

'''

import re

pattern = re.compile("([a-z]+) ([a-z]+)", re.I)

m = pattern.match("Hello world Hello Python")

print(m.group(0))#打印所有子串
print(m.group(1))
print(m.group(2))

print(m.span(1))#打印第一个子串的起始结束位置