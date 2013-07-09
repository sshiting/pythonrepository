# -*- coding:utf-8 -*-
#
#   Author  :   sushiting
#   E-mail  :   sushiting@163.com
#   Date    :   2013-7-9
#   Desc    :   列表综合
#
intArr = [1,2,3,4,5]
newIntArr = [3*i for i in intArr if i%2==0]
print newIntArr

#在函数中接收元组和列表
#当要使函数接收元组或字典形式的参数的时候，有一种特殊的方法，它分别使用*和**前缀。
#这种方法在函数需要获取可变数量的参数的时候特别有用。
def powsersum(power,*args):
    total = 0
    for i in args:
        total += pow(power, i)
    return total
print powsersum(2,1,3,4),powsersum(1,1,2,3,4,5)
def printmaps(args):
    print args
    for i in args:
        print args[i]
printmaps({"name":"sushiting"})

#以下较为特殊  **
def testdict(**args):
    print args
testdict(a=3,b=3)