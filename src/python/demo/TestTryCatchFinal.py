# -*- coding:utf-8 -*-
#
#   Author  :   sushiting
#   E-mail  :   sushiting@163.com
#   Date    :   2013-7-8
#   Desc    :   
#
try:
    s = raw_input("enter something:")
    s = int(s)
    print s/1
except EOFError:
    print "EOFerror"
except:
    print "something is error"
else:
    print "it don't rais exception"
finally:
    print "this is final block"
