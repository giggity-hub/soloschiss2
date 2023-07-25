import os
import json
import random
import sys
import glob
from importlib.machinery import SourceFileLoader
import json
from pathlib import Path
from sklearn.model_selection import train_test_split

from domains.domains import load_domain_sampler
from domains.domains import domains_dict

# this_dir = Path(os.path.dirname(__file__))
# parent_dir = this_dir.parent.absolute()

# DATA_DIR = os.path.join(this_dir, 'stuttbard', 'data')
# OUT_DIR = os.path.join(this_dir, 'data')
DATA_DIR = './stuttbard/data'
OUT_DIR = './data'

class format_dictizzly_bizzl(dict):
    def __missing__(self, key):
        return "%(" + key + ")s"
    

train_sampler, test_sampler = load_domain_sampler(domains_dict)

def get_samples(samplers_dict: dict):
    
    format_dict = {key : sampler.sample() for (key, sampler) in samplers_dict.items()}

    res = {}
    for key, value in format_dict.items():
        if "," in key:
            sub_keys = key.split(',')
            sub_keys = [sub_key.strip() for sub_key in sub_keys]
            sub_key_sub_val_pairs = zip(sub_keys, value)
            sub_keys_dict = dict(sub_key_sub_val_pairs)
            res = {**res, **sub_keys_dict}

        else:
            res[key] = value
    
    return res


def _parametrize(config):
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
                format_dict = get_samples(config['samplers'])
                new_moped = format_dictizzly_bizzl(format_dict)
                sample = {key : value % new_moped for (key, value) in sample.items()}

            res.append(sample)

    return res

def get_samplers(sampler_accesors, sampler):
    # print(sampler_accesors)
    return {key : fn(sampler) for (key, fn) in sampler_accesors.items()}


def parametrize(config):
    random.shuffle(config['user_system'])
    train_tuples, test_tuples = train_test_split(config['user_system'], test_size=0.25)

    train_config = {
        "user_system": train_tuples,
        "belief": config['belief'],
    }

    test_config = {
        "user_system": test_tuples,
        "belief": config['belief'],
    }
    if 'samplers' in config:
        train_config['samplers'] = get_samplers(config['samplers'], train_sampler)
        test_config['samplers'] = get_samplers(config['samplers'], test_sampler)

    return _parametrize(train_config), _parametrize(test_config)





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


def save_data(data, out_path):
    # out_path = os.path.join(out_dir, "data.json")
    with open(out_path, 'w+') as f:
        json.dump(data, f, indent=4)

def convert_python_files():
    train_data = []
    test_data = []
    
    for (dir_path, dir_names, file_names) in os.walk(DATA_DIR):
        # file_paths = [os.path.join(dir_path, name) for name in file_names]
        python_files_in_dir = glob.glob(dir_path + '/*.py')

        for python_file_path in python_files_in_dir:
            with open(python_file_path) as f:
                file_name = os.path.basename(python_file_path)
                module_name, _ = os.path.splitext(file_name)

                tmp_module = SourceFileLoader(module_name, python_file_path).load_module()

                # spec.loader.exec_module(foo)
                json_res = tmp_module.main(parametrize)

                for moped in json_res:
                    # print(moped)
                    train_data += moped[0]
                    # if len(moped) > 1:
                    test_data += moped[1]

    return train_data, test_data

if __name__ == "__main__":
    # 1.) Save the output of all python files to json files
    file_name = sys.argv[1]
    train_data, test_data = convert_python_files()

    # data = load_data()
    test_data = list(map(to_soloist_format, test_data))
    train_data = list(map(to_soloist_format, train_data))
    out_path_train = os.path.join(OUT_DIR, f"{file_name}_train.json")
    out_path_test = os.path.join(OUT_DIR, f"{file_name}_test.json")
    save_data(train_data, out_path_train)
    save_data(test_data, out_path_test)

    print(f"You have {len(train_data)} training samples and {len(test_data)} test samples")