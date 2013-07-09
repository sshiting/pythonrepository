# -*- coding:utf-8 -*-
#
#   Author  :   sushiting
#   E-mail  :   sushiting@163.com
#   Date    :   2013-7-5
#   Desc    :   控制流程IF/ELSE,WHILE,FOR
#
name = 'sushiting'
if name == 'sushiting':
    print "it's me"
else:
    print "it's not me"
# for n in range(1,100):
#     if n%3==0:
#         print n;
# 输出九九乘法表
i=1
while i<10:
    for j in range(1,i+1):
        print '%d*%d=%d'%(i,j,i*j),
        if j==i:
            print
    i=i+1;