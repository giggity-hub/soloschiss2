import os
import json
import random
import sys
import glob
from importlib.machinery import SourceFileLoader
import json
from pathlib import Path
from sklearn.model_selection import train_test_split
from typing import NamedTuple

from domains.domains import load_domain_sampler
from domains.domains import domains_dict
import re

# this_dir = Path(os.path.dirname(__file__))
# parent_dir = this_dir.parent.absolute()

# DATA_DIR = os.path.join(this_dir, 'stuttbard', 'data')
# OUT_DIR = os.path.join(this_dir, 'data')
DATA_DIR = './stuttbard/data_multiturn'
OUT_DIR = './data'

class format_dict(dict):
    def __missing__(self, key):
        return "%(" + key + ")s"
    

train_sampler, test_sampler = load_domain_sampler(domains_dict)

def get_samples(samplers_dict: dict):
    
    fd = {key : sampler.sample() for (key, sampler) in samplers_dict.items()}

    res = {}
    for key, value in fd.items():
        if "," in key:
            sub_keys = key.split(',')
            sub_keys = [sub_key.strip() for sub_key in sub_keys]
            sub_key_sub_val_pairs = zip(sub_keys, value)
            sub_keys_dict = dict(sub_key_sub_val_pairs)
            res = {**res, **sub_keys_dict}

        else:
            res[key] = value
    
    return format_dict(res)







prefix_system = lambda x : 'system : ' + x
prefix_user = lambda x : 'user : ' + x
prefix_belief = lambda x : 'belief : ' + x




def save_data(data, out_file):
    out_path = os.path.join(OUT_DIR, out_file)
    with open(out_path, 'w+') as f:
        json.dump(data, f, indent=4)


class DialogueTurn:
    def __init__(self, user: str, system: str, belief: str = "") -> None:
        all_parameters_are_strings = (type(user) is str) and (type(system) is str) and (type(belief) is str)
        if not all_parameters_are_strings: 
            raise ValueError("Not all arguments for user system and belief are of type str")

        self.user = f"user : {user}"
        self.system = f"system : {system}"
        self.belief = f"belief : {belief}" if len(belief) > 0 else ""


def to_soloist_format(dt: DialogueTurn):
    soloist_dict = {
        "history": [dt.user],
        "belief": dt.belief,
        "kb": "",
        "reply": dt.system
    }
    return soloist_dict

def find_samples(text: str):
    pattern = '{[a-z_]+}'
    # Matches all occurrences of the form %(...)s
    template_slots = [m.group() for m in re.finditer(pattern, text)]
    # Retreive only slot key e.g %(restaurant_name)s => restaurant_name
    template_slot_keys = [ts[1:-1] for ts in template_slots]
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


def parametrize(turn: DialogueTurn, fd: format_dict):
    turn.user = turn.user.format(**fd)
    turn.belief = turn.belief.format(**fd)
    turn.system = turn.system.format(**fd)
    return turn

def fill_samples(turn: DialogueTurn, sampler: dict):
    keys = find_samples("".join([turn.user, turn.system, turn.belief]))
    sampler_keys = get_sampler_keys(keys, sampler)
    samplers = {k: sampler[k] for k in sampler_keys}
    fd = get_samples(samplers)

    return parametrize(turn, fd)

def fill_history_samples(histories, sampler):
    for i in range(len(histories)):
        history = histories[i]
        foreach = lambda h : fill_samples(DialogueTurn(*h), sampler)
        histories[i] = list(map(foreach, history))

    return histories

def convert_python_files():
    train_data = []
    test_data = []
    
    for (dir_path, dir_names, file_names) in os.walk(DATA_DIR):
        python_files_in_dir = glob.glob(dir_path + '/*.py')

        for python_file_path in python_files_in_dir:
            with open(python_file_path) as f:
                file_name = os.path.basename(python_file_path)
                module_name, _ = os.path.splitext(file_name)

                tmp_module = SourceFileLoader(module_name, python_file_path).load_module()

                histories = tmp_module.main()
                histories_train, histories_test = train_test_split(histories, test_size=0.25)
                train_data += fill_history_samples(histories_train, train_sampler)
                test_data += fill_history_samples(histories_test, test_sampler)
                

    return train_data, test_data

def convert_to_single_turn(histories):
    res = []
    for history in histories:
        for dialogue_turn in history:
            res.append(to_soloist_format(dialogue_turn))

    return res

def convert_to_multi_turn(dialogues):
    res = []
    for dialogue in dialogues:
        history = []
        for turn in dialogue:
            history.append(turn.user)
            res.append({
                "history": [*history],
                "kb": "",
                "belief": turn.belief,
                "reply": turn.system
            })
            history.append(turn.system)
    return res


if __name__ == "__main__":
    # 1.) Save the output of all python files to json files
    file_name = sys.argv[1]
    train_data, test_data = convert_python_files()

    test_data_single_turn = convert_to_single_turn(test_data)
    test_data_multi_turn = convert_to_multi_turn(test_data)

    train_data_single_turn = convert_to_single_turn(train_data)
    train_data_multi_turn = convert_to_multi_turn(train_data)
    
    

    # out_path_train = os.path.join(OUT_DIR, f"{file_name}_train.json")
    # out_path_test = os.path.join(OUT_DIR, f"{file_name}_test.json")
    save_data(train_data_single_turn, f"{file_name}_train_single.json")
    save_data(train_data_multi_turn, f"{file_name}_train_multi.json")

    save_data(test_data_single_turn, f"{file_name}_test_single.json")
    save_data(test_data_multi_turn, f"{file_name}_test_multi.json")

    # print(f"You have {len(train_data)} training samples and {len(test_data)} test samples")