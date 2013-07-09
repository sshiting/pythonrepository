# -*- coding:utf-8 -*-
#
#   Author  :   sushiting
#   E-mail  :   sushiting@163.com
#   Date    :   2013-7-8
#   Desc    :   
#
class TestClass:
    #name类似java的静态变量
    #self 相当于类的一个实例  (属性的定义一般放在self中)
    name = 'sushiting'
    age = 23
    def __init__(self):
        print 'this is a class'
    def say(self):
        print 'hello'
    def setName(self,name):
        self.name = name
    def addAge(self,num):
        self.age = self.age + num
    def getName(self):
        print self.name
test = TestClass()
test.say()
test.setName("jack")
test.getName()
print "age:%s" %TestClass.age
test.addAge(3)
print "age:%s" %test.age
test2 = TestClass()
print "age:%s" %TestClass.age
