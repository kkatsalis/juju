   94  sudo add-apt-repository ppa:juju/stable
   95  sudo apt-get update && sudo apt-get install juju-core
   96  sudo apt-get install juju-core
   97  sudo apt-get install juju-local
  100  sudo add-apt-repository ppa:juju/stable
  101  sudo apt-get install juju-core
  102  sudo apt-get install juju-local
  104  juju swtich local
  105  juju switch local
  106  sudo apt-get install juju-local
  109  juju generate-config 
  110  juju switch local
  111  juju bootstrap
  113  vim .juju/environments.yaml 
  115  juju status --format=tabular
  117  juju charm get oai-hss
  118  juju charm get oai-epc
  119  juju deploy mysql
  120  juju status --format=tabular
  130  juju status --format=tabular
  135  juju deploy --repository ~/charmproject local:trusty/oai-hss 
  136  juju deploy juju-gui
  137  juju remove-service mysql
  138  juju deploy mysql
  139  juju remove-service oai-hss
  140  juju remove-service mysql
  141  juju remove-service oai-hss
  144  juju set mysql dataset-size='256M'
  145  juju deploy mysql 
  146  juju deploy oai-hss oai-hss0
  147  juju deploy --repository ~/charmproject local:trusty/oai-hss oai-hss0 
  148  juju set mysql dataset-size='256M'
  149  juju remove-service mysql
  150  juju
  151  juju help
  152  juju help commands
  153  juju remove-service oai-hss0
  154  juju set mysql dataset-size='256M'
  170  juju debug-hooks  mysql
  171  juju debug-hooks  mysql/0 
  172  juju debug-hooks  oai-hss/0 
  173  juju status --format=tabular
  174  watch -n 1 juju status --format=tabular
  175  watch -n 2 juju status --format=tabular
  176  watch  juju status --format=tabular
  182  juju resolved --retry mysql
  183  juju resolved --retry mysql/0 
  184  juju resolved  mysql/0
  185  vim .juju/environments/local.jenv 
  186  juju resolved  mysql/0
  187  less .juju/ssh/juju_id_rsa
  188  juju resolved  mysql/1
  189  juju resolved --retry mysql/2 
  190  juju resolved --retry oai-hss/0 
  191  juju resolved oai-hss/0 
  192  juju resolved --retry oai-hss0/0 
  193  juju resolved oai-hss/0 
  194  juju resolved  mysql/2 
  195  juju resolved --retry oai-hss0 
  196  juju resolved --retry oai-hss0/0
  197  juju resolved  oai-hss0/0
  606  juju resolved  oai-enb/0
  607  juju resolved  oai-rrh/5
  608  juju -help
  609  juju --version
  618  juju add-relation mysql oai-hss
  620  juju resolved oai-hss/1
  621  juju add-relation oai-epc oai-hss
  644  history | grep juju
  645  juju destroy-machine --force 0/kvm/4 
  646  juju help deploy
  647  history | grep juju
  648  juju remove-service oaisim-enb-ue
  649  juju resolved oaisim-enb-ue/1
  650  juju debug-log
  651  juju destroy-machine --force 0/kvm/4 
  652  juju destroy-machine --force 0/kvm/5 
  653  juju destroy-machine --force 0/kvm/2 
  654  juju destroy-machine --force 0/kvm/3
  655  juju destroy-machine --force 0/kvm/2
  656  juju destroy-machine --force 0/kvm/1
  657  juju remove-service oaisim-enb-ue
  658  juju remove-service oai-hss
  659  juju remove-service oai-epc
  660  juju remove-service oai-mysql
  661  juju remove-service mysql
rm -rf /etc/init/juju*
rm -rf /var/lib/juju
  663  history | grep juju > juju.cmd


#!/bin/bash

#consider to have modified the environment.yaml file in order to bootstrap juju
#on a physical machine(see the slide "Manual_provisioning")
#So you have machine 0 inside the environment that is use for the juju state server
#to take care about the whole environment. You can't deploy on that machine without
#virtualization otheriwise there will be a conflict between charms and juju state 
#server.But you can deploy on different KVMs. With the option "--to kvm:0" the manual
#enviroment will automatically setup a kvm inside the physical machine "0"

juju deploy --to kvm:0 juju-gui
juju deploy --to kvm:0 mysql
juju deploy --to kvm:0 phpmyadmin
juju deploy --to kvm:0 --repository ~/charmproject local:trusty/oai-hss
juju deploy --to kvm:0 --repository ~/charmproject local:trusty/oai-epc
#Since for the oaisim and oaienb you need first a machine, you can let the
#manual env to create a kvm and immediately deploy a charm, so we need to add 
#a kvm on machime "0" that will be created automatically by the manual env, but
# now we have time to tune it. After you need to deploy by addressing explicitely
#that machine.
juju add-machine --to kvm:0
echo "Cannot procede with the oaisim deployment...Use virt-manager to pass the cpu flags and tune the machine(4G memory AND 3 CPUs)...then deploy by addressing that machine"
exit 0
#After you have tuned your machine you can deploy oaisim
juju deploy --to 0/kvm/5 --repository ~/charmproject local:trusty/oaisim

#Now we want a machine to deploy oaienb
juju add-machine --to kvm:0
echo "Cannot procede with the oaienb deployment...Use virt-manager to pass the cpu flags and tune the machine(4G memory AND 3 CPUs)...then deploy by addressing that machine"
exit 0
#
juju deploy --to 0/kvm/6 --repository ~/charmproject local:trusty/oai-enb

juju add-relation mysql phpmyadmin
juju add-relation mysql oai-hss
juju add-relation oai-hss oai-epc
juju add-relation oaisim oai-epc
juju add-relation oai-enb oai-epc



juju destroy-machine --force 1/lxc/0

