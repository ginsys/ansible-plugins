# (c) 2013, Ali-Akber Saifee <ali@indydevs.org>

import ansible.errors as errors
from ansible.utils import safe_eval


class LookupModule(object):

    def __init__(self, basedir=None, **kwargs):
        self.basedir = basedir

    def run(self, terms, inject=None, **kwargs):
        terms = safe_eval(terms)

        if not isinstance(terms, dict):
            print terms
            raise errors.AnsibleError("with_hash_items expects a dict")
        return [{"key": term[0], "value": term[1]} for term in terms.items()]
