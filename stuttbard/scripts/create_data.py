import os
import json
import random
import sys
import glob
from importlib.machinery import SourceFileLoader
import json
from pathlib import Path

from stuttbard.domains.sampler import create_sampler

this_dir = Path(os.path.dirname(__file__))
parent_dir = this_dir.parent.absolute()

DATA_DIR = os.path.join(parent_dir, 'data')
OUT_DIR = parent_dir

class format_dictizzly_bizzl(dict):
    def __missing__(self, key):
        return "%(" + key + ")s"
    

def parametrize(config):
    n_repetitions = config['n_repetitions'] if 'n_repetitions' in config else 1
    belief = config['belief']
    res = []
    for d in config["user_system"]:
        for i in range(n_repetitions):
            
            sample = {
                "user": d[0],
                "belief": belief,
                "system": d[1]
            }

            if 'samplers' in config:
                samplers = config['samplers']
                format_dict = {key : sampler.sample() for (key, sampler) in samplers.items()}

                new_moped = {}
                for key, value in format_dict.items():
                    if type(value) == list or type(value) == tuple:
                        sub_keys = key.split(',')
                        new_moped = {**new_moped, **dict(zip(sub_keys, value))}
                    else:
                        new_moped[key] = value
                
                new_moped = format_dictizzly_bizzl(new_moped)
                sample = {key : value % new_moped for (key, value) in sample.items()}

            res.append(sample)

    return res

prefix_system = lambda x : 'system : ' + x
prefix_user = lambda x : 'user : ' + x
prefix_belief = lambda x : 'belief : ' + x

def to_soloist_format(compact_dict):
    soloist_dict = {
        "history": [prefix_user(compact_dict['user'])],
        "belief": prefix_belief(compact_dict["belief"]),
        "kb": "",
        "reply": prefix_system(compact_dict["system"])
    }
    return soloist_dict


def load_data():
    data = []
    for (dir_path, dir_names, file_names) in os.walk(DATA_DIR):
        json_files = glob.glob(dir_path + '/*.json')


        for file_path in json_files:
            with open(file_path) as f:
                data += json.load(f)

    return data

def save_data(data, out_dir):
    out_path = os.path.join(out_dir, "data.json")
    with open(out_path, 'w+') as f:
        json.dump(data, f, indent=4)

def convert_python_files():
    domain_sampler = create_sampler()
    for (dir_path, dir_names, file_names) in os.walk(DATA_DIR):
        # file_paths = [os.path.join(dir_path, name) for name in file_names]
        python_files_in_dir = glob.glob(dir_path + '/*.py')

        for python_file_path in python_files_in_dir:
            with open(python_file_path) as f:
                file_name = os.path.basename(python_file_path)
                module_name, _ = os.path.splitext(file_name)


                tmp_module = SourceFileLoader(module_name, python_file_path).load_module()

                # spec.loader.exec_module(foo)
                json_result = tmp_module.main(domain_sampler, parametrize)
            
            json_path = os.path.join(dir_path, module_name + '.json')

            with open(json_path, 'w+') as f:
                json.dump(json_result, f, indent=4)



if __name__ == "__main__":
    # 1.) Save the output of all python files to json files
    convert_python_files()
    data = load_data()
    random.shuffle(data)
    data = list(map(to_soloist_format, data))
    save_data(data, OUT_DIR)
