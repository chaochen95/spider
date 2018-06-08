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

findall(str, begin, end)
pattern.findall()#所有的全部匹配，返回列表

pattern.finditer()#所有的全部匹配，返回的使是一个迭代器

split(str, count)#切割次数
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

pattern2 = re.compile(r"\d+")
m2 = pattern2.search(r"aaa123bbb456", 2, 5)
print(m2.group())

pattern3 = re.compile(r"\d+")
m3 = pattern3.findall(r"hello 123456 789")
print(m3)

pattern4 = re.compile("[\s\d\\\;]+")#按字符集中有的切割
m4 = pattern4.split(r"a bb\aa; mm;  a")
print(m4)

pattern5 = re.compile(r"(\w+) (\w+)")#按字符集中有的切割
str = "hello 123, hello 456"
m5 = pattern5.sub("aaa bbb", str)
print(m5)