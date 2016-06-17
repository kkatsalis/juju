import json

from types import *

###############################################
#   Assert Statement
#   The syntax for assert is:
#   assert Expression[, Arguments]
#
#   -- You can use $ py.test test_assert1.py
#   -- If Python is started with the -O option,
#      then assertions will be stripped out and not evaluated
#      #python -O file.py 

###############################################

def env_status():
    print('\n\n********************  Environment Status\n')
    obj=9
    assert type(obj) is DictType, "obj is not a dictionary" 
    print json.dumps(obj, indent=2)  #same as before but beautiful
    return

#env_status()


def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32

#print KelvinToFahrenheit(273)
print KelvinToFahrenheit(-5)
