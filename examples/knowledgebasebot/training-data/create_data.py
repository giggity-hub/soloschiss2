import os
import json
import random

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


def load_data(data_dir = './data'):
    data = []
    for (dir_path, dir_names, file_names) in os.walk(data_dir):
        file_paths = [os.path.join(dir_path, name) for name in file_names]


        for file_path in file_paths:
            with open(file_path) as f:
                data += json.load(f)

    return data

def save_data(data, out_file = "data.json"):
    with open(out_file, 'w+') as f:
        json.dump(data, f, indent=4)



data = load_data()
print(len(data))
random.shuffle(data)
data = list(map(to_soloist_format, data))
save_data(data)
