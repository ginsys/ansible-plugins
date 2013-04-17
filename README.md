ansible-plugins
===============

My custom modules for ansible (https://github.com/ansible/ansible) configuration management: 
a multi-node deployment/orchestration, and remote task execution system.

This repo is ordered by the subdirectories as mentioned in ansible's lib/ansible/utils/plugins.py
```python
action_loader     = PluginLoader('ActionModule',   'ansible.runner.action_plugins',     C.DEFAULT_ACTION_PLUGIN_PATH,           'action_plugins')
callback_loader   = PluginLoader('CallbackModule', 'ansible.callback_plugins',          C.DEFAULT_CALLBACK_PLUGIN_PATH,   'callback_plugins')
connection_loader = PluginLoader('Connection',     'ansible.runner.connection_plugins', C.DEFAULT_CONNECTION_PLUGIN_PATH, 'connection_plugins', aliases={'paramiko': 'paramiko_ssh'})
module_finder     = PluginLoader('',               '',                                  C.DEFAULT_MODULE_PATH,            'library')
lookup_loader     = PluginLoader('LookupModule',   'ansible.runner.lookup_plugins',     C.DEFAULT_LOOKUP_PLUGIN_PATH,     'lookup_plugins')
vars_loader       = PluginLoader('VarsModule',     'ansible.inventory.vars_plugins',    C.DEFAULT_VARS_PLUGIN_PATH,       'vars_plugins')
filter_loader     = PluginLoader('FilterModule',   'ansible.runner.filter_plugins',     C.DEFAULT_FILTER_PLUGIN_PATH,     'filter_plugins')
```

+ `action_plugins/`
+ `callback_plugins/`
+ `connection_plugins/`
+ `library/`    (action modules, those which get transferred and executed to the target host)
+ `lookup_plugins/`
+ `vars_plugins/`
+ `filter_plugins/`
+ `inventory_plugins`    (No part of ansible's base code; [as described in ansible's api docs](https://github.com/ansible/ansible/blob/devel/docsite/latest/rst/api.rst#external-inventory-scripts))

contributing
============

If you'd like to contribute your modules, or patch existent modules, please send a pull request.
Be sure however 
* to send your pull request from a **feature branch**, derived from the `devel` branch
* one (set of) plugin file(s) per commit only!
  * e.g. a set: action_plugins and library/ modules form a pair

