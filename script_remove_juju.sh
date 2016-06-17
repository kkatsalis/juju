#!/bin/bash
sudo rm -rf /etc/init/juju*
sudo rm -rf /var/lib/juju
sudo rm -rf .juju/
juju generate-config
juju switch local
sudo pkill jujud
sudo pkill mongod
#vim .juju/environments.yaml
