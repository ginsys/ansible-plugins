# Ansible lookup plugin for using hashes of arrays structures in loops
# (c) 2014, Sebastien Bocahu <zecrazytux@zecrazytux.net>

# For each item of the value (array) of each hash item, returns the hash
# key and the array item. Example:
#
# - authorized_keys:
#    root:
#      - admin1
#    www-data:
#      - dev1
#      - dev2
#
# - ssh_keys:
#    admin1: ssh-rsa ...
#    dev1: ssh-rsa ...
#    dev2: ssh-rsa ...
#
# - name: set authorized_keys
#  authorized_key: user="{{ item.key }}" key="{{ ssh_keys[item.value] }}"
#  with_hashrays: authorized_keys

import ansible.utils as utils
import ansible.errors as errors

class LookupModule(object):

    def __init__(self, basedir=None, **kwargs):
        self.basedir = basedir

    def run(self, terms, inject=None, **kwargs):
        terms = utils.listify_lookup_plugin_terms(terms, self.basedir, inject)

        if not isinstance(terms, dict):
            raise errors.AnsibleError("with_hashrays expects a dict of arrays")

        ret = []
        for k,v in terms.iteritems():
            if isinstance(v, list):
                for vv in v:
                    ret.append({'key': k, 'value': vv})

        return ret
