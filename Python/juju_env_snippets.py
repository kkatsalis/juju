import json

from types import *
from jujuclient import Environment

env = Environment.connect('local')

#######################################
#           General Functions
#######################################

def env_facades():
	print('********************  Facades\n')
	obj=env.facades
	assert type(obj) is DictType, "obj is not a dictionary" 
	print(obj)
	return


def env_users():
	print('\n\n********************  Users\n')
	obj=env.users.list()
	assert type(obj) is DictType, "obj is not a dictionary" 
	print(obj)
	return
  
def env_charms():
	print('\n\n********************  Charms\n')
	obj=env.charms.list()
	assert type(obj) is DictType, "obj is not a dictionary"
	assert type(obj) is DictType, "obj is not a dictionary" 
	print(obj)
	return

#######################################
#           Environment Commands
#######################################
def env_config():
	print('\n\n********************  Environment Config\n')
	obj=env.get_env_config()
	assert type(obj) is DictType, "obj is not a dictionary"
	print(obj)
	return

def env_constraints():
	print('\n\n********************  Environment Constraints\n')
	obj=env.get_env_constraints()
	assert type(obj) is DictType, "obj is not a dictionary" 
	print(obj)
	return

def enf_info():
	print('\n\n********************  Environment Info\n')
	obj=env.info()
	assert type(obj) is DictType, "obj is not a dictionary" 
	print(obj)
	print json.dumps(obj, indent=2)  #same as before but beautiful
	return

def env_status():
	print('\n\n********************  Environment Status\n')
	obj=env.status()
	assert type(obj) is DictType, "obj is not a dictionary" 
	print json.dumps(obj, indent=2)  #same as before but beautiful
	return

