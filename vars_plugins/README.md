ansible-plugins
===============

My custom modules for ansible (https://github.com/ansible/ansible) configuration management: 
a multi-node deployment/orchestration, and remote task execution system.

This repo is ordered by the subdirectories as mentioned in ansible's lib/ansible/utils/plugins.py
```python
vars_loader       = PluginLoader('VarsModule',     'ansible.inventory.vars_plugins',    C.DEFAULT_VARS_PLUGIN_PATH,       'vars_plugins')
```
+ `vars_plugins/`
    + group_vars_dirs.py: customized version of the original `lib/ansible/inventory/vars_plugins/group_vars.py`
        - With this plugin you can organise group and host vars files in various subdirectories, as you like. 
	- Files directly beneath host_vars or group_vars are ignored, as those are handled by group_vars.py in core.
        - Files are named to the group name, and can haven optionally an extension .yml or .yaml
        - There can be only one (1) file per group or host, otherwise an error is thrown.

