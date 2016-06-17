import json

from types import *
from jujuclient import Environment

env = Environment.connect('local')

#############################################################
#           General   Environment Functions
#			Assuming: env = Environment.connect('local')
#############################################################

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
	print(obj)
	return


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
 


#############################################################
#           Machine Functions
#			Assuming: env = Environment.connect('local')
#############################################################

# Add Machines - Examples of parametes tested  
# param={'series':'','constraints':{},'machine_spec':'', 'parent_id':'','container_type':''}
# param={'series':'','constraints':{},'machine_spec':'', 'parent_id':'4','container_type':'kvm'}
# param={'series':'','constraints':{'cpu-cores':1,'mem':1},'machine_spec':'', 'parent_id':'','container_type':''}

def env_add_machine(param):
    assert type(param) is DictType, "Parameters is not a dictionary"
    env.add_machine(series=param['series'], constraints=param['constraints'], 
                    machine_spec=param['machine_spec'], parent_id=param['parent_id'], 
                    container_type=param['container_type'])
    
    print "Machine added with parameters",param
    return

# Delete Machines - Examples of parametes tested  
# machine_ids=['2','3']
def env_destroy_machines(machine_ids):
    assert type(machine_ids) is ListType, "machine_ids is not a list" 
    env.destroy_machines(machine_ids, force=False)
    print "machines deleted: ", machine_ids
    return  



#############################################################
#           Service Functions
#			Assuming: env = Environment.connect('local')
#############################################################

# Add Service - Examples of parametes tested  
# param={'service_name':'mysql','charm_url': 'cs:trusty/mysql-6', 'num_units':1, 'config':{}, 'constraints':{}, 'machine_spec':None}
   
def env_add_service(param):
    assert type(param) is DictType, "Parameters is not a Dictionary"
    
    env.deploy(service_name=param['service_name'], charm_url=param['charm_url'], num_units=param['num_units'], 
               config=param['config'], constraints=param['constraints'],machine_spec=param['machine_spec'])
    
    print "Service deployed with parameters",param
    return


# Delete Service - Examples of parametes tested  
# service_name="mysql"
# env_destroy_service(service_name)


def env_destroy_service(service_name):
    assert type(service_name) is StringType, "service_name is not a String" 
    env.destroy_service(service_name)
    print "service deleted: ",service_name 
    return  













