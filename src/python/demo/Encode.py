# -*- coding: utf-8 -*-
# 用于解决gvim控制台输出乱码
import sys
reload(sys)
class UnicodeStreamFilter:
    def __init__(self, target):
        self.target = target
        self.encoding = 'utf-8'
        self.errors = 'replace'
        self.encode_to = 'cp936'
    def write(self, s):
        if type(s) == str:
            s = s.decode("utf-8")
        s = s.encode(self.encode_to, self.errors).decode(self.encode_to)
        self.target.write(s)
sys.setdefaultencoding('cp936')  # @UndefinedVariable
sys.stdout = UnicodeStreamFilter(sys.stdout)
if __name__ == "__main__":
    print '苏'


