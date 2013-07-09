# -*- coding:utf-8 -*-
#
#   Author  :   sushiting
#   E-mail  :   sushiting@163.com
#   Date    :   2013-7-9
#   Desc    :   强大的匿名函数 lambda args:expression 其中args为参数，expression为表达式
#
def make_repeater(n):
    return lambda args:args*n
twice = make_repeater(2)
print twice(2)
print twice("sushiting")

#Python中，如果函数体是一个单独的return expression语句，
#开发者可以选择使用特殊的lambda表达式形式替换该函数：lambda parameters: expression
aList = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
low = 3
high = 7
filter(lambda x, l=low, h=high: h>x>l, aList) 
nalist = [i for i in aList if 3<i and i<7]
print nalist
# returns: [4, 5, 6]

fun = lambda x:pow(3,x)
print fun(3)