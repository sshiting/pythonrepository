# -*- coding:utf-8 -*-
#
#   Author  :   sushiting
#   E-mail  :   sushiting@163.com
#   Date    :   2013-7-8
#   Desc    :   
#
class SchoolMember(object):
    """Docstring for MySchoolMemberass """

    def __init__(self,name,sex):
        """@todo: to be defined1 """
        self.name = name
        self.sex = sex
    def tell(self):
        print 'Name:"%s"'%(self.name)
class Teacher(SchoolMember): 
    """Docstring for Teacher """
    def __init__(self,name,sex,salary):
        """@todo: to be defined1
        :name: @todo
        :sex: @todo
        """
        SchoolMember.__init__(self,name,sex)
        self._name = name
        self._sex = sex        
        self.level = 'teacher'
        self.sex = 'women'
        self.salary = salary
    def tell(self):
        print 'Name:%s,Salary:%s'%(self.name,self.salary)
class Student(SchoolMember):
    """Docstring for Studnet """

    def __init__(self,name,age,mark):
        """@todo: to be defined1 """
        SchoolMember.__init__(self,name,age)
        self.mark = mark
    def tell(self):
        print "Name:%s,Mark:%s"%(self.name,self.mark)
teacher = Teacher('Mrs Zhang','men','3500/mon')
student = Student('sushiting','men',100)
member = [teacher,student]
for m in member:
    m.tell()
        
print member
print student.tell()
