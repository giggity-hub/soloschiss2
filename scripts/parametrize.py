from typing import List
from scripts.types import Dialogue, DialogueTurn
import re

def create_format_dict_for_samplers(samplers_dict: dict):
    """This function creates a format dict which can be used to format a string from a dictionary of samplers.
    The format dict will contain one entry for every key or subkey of the sampler.
    e.g {'index_str, index_int': ...} => {'index_str': ..., 'index_int: ...}

    Args:
        samplers_dict (dict): _description_

    Returns:
        _type_: _description_
    """
    keyvals = []
    for sampler_key, sampler in samplers_dict.items():
        sample = sampler.sample()
        if ", " in sampler_key:
            sub_keys = sampler_key.split(", ")
            keyvals += zip(sub_keys, sample)
        else:
            keyvals.append((sampler_key, sample))

    return dict(keyvals)


def find_sample_slot_keys(text: str) -> List[str]:
    """This function finds all sample slots e.g {domain_name} or {index_int} and returns a list of all requested samplers
    example "{domain_name} {index_int}" => ["domain_name", "index_int"]

    Args:
        text (str): _description_

    Returns:
        _type_: _description_
    """
    pattern = '{[a-z_]+}'
    # Matches all occurrences of the form {...}
    template_slots = [m.group() for m in re.finditer(pattern, text)]
    # Retreive only slot key e.g {restaurant_name} => restaurant_name
    template_slot_keys = [ts[1:-1] for ts in template_slots]
    # Each sampler should be sampled only once per dialogue turn
    unique_template_slot_keys = list(set(template_slot_keys))
    return unique_template_slot_keys

def get_sampler_keys(subkeys, sampler):
    subkey_to_key = {k: key for key in sampler.keys() for k in key.split(', ') }
    keys_res = []
    for subkey in subkeys:
        if subkey not in subkey_to_key:
            exception_msg = f"The value {subkey} is not a valid key for parametrization"
            raise Exception(exception_msg)
        else:
            keys_res.append(subkey_to_key[subkey])
        
                
    return list(set(keys_res))


def parametrize(turn: DialogueTurn, fd: dict) -> DialogueTurn:
    user = turn.user.format(**fd)
    belief = turn.belief.format(**fd)
    system = turn.system.format(**fd)
    return DialogueTurn(user, system, belief)

def fill_samples(turn: DialogueTurn, sampler: dict):
    keys = find_sample_slot_keys("".join([turn.user, turn.system, turn.belief]))
    sampler_keys = get_sampler_keys(keys, sampler)
    samplers = {k: sampler[k] for k in sampler_keys}
    fd = create_format_dict_for_samplers(samplers)

    return parametrize(turn, fd)

def parametrize_dialogues(dialogues: List[Dialogue], sampler):
    res = []
    for i in range(len(dialogues)):
        dialogue = dialogues[i]
        res.append([])
        for j in range(len(dialogue)):
            turn = dialogue[j]
            try:
                res[i].append(fill_samples(turn, sampler))
            except:
                print("omitted 1 input because of faulty format")
            

    return res