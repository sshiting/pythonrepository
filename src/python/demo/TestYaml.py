# -*- coding:utf-8 -*-
#
#   Author  :   sushiting
#   E-mail  :   sushiting@163.com
#   Date    :   2013-8-2
#   Desc    :   
#
import yaml
children = {'count':3,'language':[{'name':'java'},{'name':'c#'},{'name':'delphi'}]}
person = {'name':'sushiting','age':'30','children':children}
print yaml.dump(person, default_flow_style=False)

print '苏世挺'
# aproject = {'name': 'Silenthand Olleander', 
#                    'race': 'Human',
#                     'traits': ['ONE_HAND', 'ONE_EYE']
#                    }


#print yaml.dump(aproject, default_flow_style=False)

#返回
#name: Silenthand Olleander
#race: Human
#traits: [ONE_HAND, ONE_EYE]
