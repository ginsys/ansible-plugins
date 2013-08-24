# (c) 2013, Ali-Akber Saifee <ali@indydevs.org>

def hash_to_tuples(h):
    return h.items()

def hash_keys(h):
    return h.keys()

def hash_values(h):
    return h.values()

def zipped_hash(h, key, item):
    ret = []
    for el in h:
        if h[el].has_key(item):
            for subel in h[el][item]:
                ret.append({"key" : h[el][key], "value" : subel })
    return ret

class FilterModule(object):
    ''' utility filters for operating on hashes '''

    def filters(self):
        return {
            'hash_to_tuples' : hash_to_tuples
            ,'hash_keys'     : hash_keys
            ,'hash_values'   : hash_values
            ,'zipped_hash'   : zipped_hash
        }

