ansible-plugins
===============

My custom modules for ansible (https://github.com/ansible/ansible) configuration management: 
a multi-node deployment/orchestration, and remote task execution system.

This repo is ordered by the subdirectories as mentioned in ansible's lib/ansible/utils/plugins.py

Inventory plugins are best written in Python, but could be in any language you like.

+ `inventory_plugins`    (No part of ansible's base code; [as described in ansible's api docs](https://github.com/ansible/ansible/blob/devel/docsite/latest/rst/api.rst#external-inventory-scripts))
    + `jvspherecontrol`: a python plugin as a frontend to [Patrick Debois' jvspherecontrol](https://github.com/jedi4ever/jvspherecontrol)
    + `known_hosts`: a python plugin to makes sure the known_hosts line is present or absent in the user's .ssh/known_hosts.
    + `seds`: a simple bash plugin which runs a `sed 's'` command

