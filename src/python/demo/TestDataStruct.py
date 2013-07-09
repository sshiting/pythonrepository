# -*- coding:utf-8 -*-
#
#   Author  :   sushiting
#   E-mail  :   sushiting@163.com
#   Date    :   2013-7-5
#   Desc    :   数据结构 python常用数据结构有如下：(列表、元组、字典 )===>序列
#

#列表 数据可以伸缩
import Encode  # @UnusedImport
shoplist = ["apple","banana","orange"]
shoplist.append("mango")
shoplist.remove("orange")
def cmpa(a,b):
    return -1;
shoplist.sort(cmp=cmpa, key=None, reverse=False)
print len(shoplist),
for fruit in shoplist:
    print fruit,
#元组 数据固定
zoo = ('woft','elephant','tiger')
new_zoo = ('bird','drogan',zoo)
print len(zoo),
print '\nold zoo:'
for animal in zoo:
    print animal,
print '\nnew zoo:'
for naimal in new_zoo:
    print naimal,
print new_zoo[2][1]
print '========='

#切片
#shoplist[:-1]会返回除了最后一个项目外包含所有项目的序列切片。
for temp in zoo[1:3]:
    print temp
#字典 (键值对，相当于Map
data = {"name":"sst","age":24}
print data["name"]
print data.get("age")


#对象复制(以下并没有实现真正的复制，真正的复制通过切片来实现)
zoo = ['woft','elephant','tiger']
print "=======对象复制======="
myzoo = zoo #切片实现 eg:  myzoo=zoo[:]
print "zoo is %s,myzoo is %s"%(zoo,myzoo)
del zoo[1]
zoo.remove('woft')
print "zoo is %s,myzoo is %s"%(zoo,myzoo)






