import json

from types import *
from jujuclient import Environment

env = Environment.connect('local')

def env_add_machine():
	print('\n\n********************  Add machine\n')
	env.add_machine(series='', constraints={'cpu-cores':1, 'cpu-power':1, 'mem':1024}, machine_spec='', parent_id='', container_type='kvm')
	return



def env_destroy_machines():
        env.destroy_machines([3], force=False)
        

env_destroy_machines()
 
#env_add_machine()
