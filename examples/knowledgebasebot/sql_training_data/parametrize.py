from itertools import product
import random
from collections.abc import Iterable


class format_dict(dict):
    def __missing__(self, key):
        return f'%({key})s'

def generate_format_dicts(conf_dict):
    permutations = product(*conf_dict.values(), repeat=1)

    res = []
    for vals in permutations:
        key_vals = []
        for key, val in zip(conf_dict.keys(), vals):
            if type(val) == tuple or type(val) == list:
                sub_keys = key.split(',')
                sub_keys = [k.strip() for k in sub_keys]
                key_vals += zip(sub_keys, val)
            else:
                key_vals.append((key, val,))
        
        fd = format_dict(key_vals)
        res.append(fd)
    
    return res

def parametrize(training_obj, conf:dict, max_len=float('+inf')):
    fds = generate_format_dicts(conf)
    res = []
    for fd in fds:
        res.append({
            "user": training_obj['user'] % fd,
            "system": training_obj['system'] % fd,
            "belief": training_obj['belief'] % fd
        })

    if len(res) > max_len:
        res = random.sample(res, max_len)
    return res


def parametrize_all(training_obj_list, conf: dict, max_len=float('+inf')):
    res = []
    for t in training_obj_list:
        res += parametrize(t, conf)
    
    if len(res) > max_len:
        res = random.sample(res, max_len)
    return res