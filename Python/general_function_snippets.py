import json

from types import *
from jujuclient import Environment

env = Environment.connect('local')

#######################################
#           General Functions
#######################################

print('********************  Facades\n')
obj=env.facades
assert type(obj) is DictType, "obj is not a dictionary" 
print(obj)


print('\n\n********************  Users\n')
obj=env.users.list()
assert type(obj) is DictType, "obj is not a dictionary" 
print(obj)
  

print('\n\n********************  Charms\n')
obj=env.charms.list()
assert type(obj) is DictType, "obj is not a dictionary"
assert type(obj) is DictType, "obj is not a dictionary" 
print(obj)

#######################################
#           Environment Commands
#######################################

print('\n\n********************  Environment Config\n')
obj=env.get_env_config()
assert type(obj) is DictType, "obj is not a dictionary"
assert type(obj) is DictType, "obj is not a dictionary" 
print(obj)


print('\n\n********************  Environment Constraints\n')
obj=env.get_env_constraints()
assert type(obj) is DictType, "obj is not a dictionary" 
print(obj)


print('\n\n********************  Environment Info\n')
obj=env.info()
assert type(obj) is DictType, "obj is not a dictionary" 
print(obj)
print json.dumps(obj, indent=2)  #same as before but beautiful



print('\n\n********************  Environment Status\n')
obj=env.status()
assert type(obj) is DictType, "obj is not a dictionary" 
print json.dumps(obj, indent=2)  #same as before but beautiful


