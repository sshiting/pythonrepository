# -*- coding:utf-8 -*-
#
#   Author  :   sushiting
#   E-mail  :   sushiting@163.com
#   Date    :   2013-7-8
#   Desc    :   类似于java的序列化，反序列化
#
#   Python提供一个标准的模块，称为pickle。使用它你可以在一个文件中储存任何Python对象，
#   之后你又可以把它完整无缺地取出来。这被称为 持久地 储存对象。
#   还有另一个模块称为cPickle，它的功能和pickle模块完全相同，只不过它是用C语言编写的，因此要快得多（比pickle快1000倍）。你可以使用它们中的任一个，而我们在这里将使用cPickle模块。记住，我们把这两个模块都简称为pickle模块。
import cPickle as p
shoplist = ['apple','orange','banana']
shopdata = file("shop.data","w")
p.dump(shoplist, shopdata)
shopdata.close()
shopdata = file("shop.data")
shoplist2 = p.load(shopdata)
print shoplist2

