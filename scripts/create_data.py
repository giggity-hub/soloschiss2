import os
import json
import random
import sys
import glob
from importlib.machinery import SourceFileLoader

from pathlib import Path
from sklearn.model_selection import train_test_split
from typing import NamedTuple
from collections import namedtuple

from domains.domains import load_domain_sampler
from domains.domains import domains_dict
import re
from typing import List, TypeAlias, Tuple

from scripts.parametrize import parametrize_dialogues, fill_samples
from scripts.types import Dialogue, DialogueTurn

DATA_DIR = './stuttbard/data_singleturn'
OUT_DIR = './data'




train_sampler, test_sampler = load_domain_sampler(domains_dict)



def save_data(data, out_file):
    out_path = os.path.join(OUT_DIR, out_file)
    with open(out_path, 'w+') as f:
        json.dump(data, f, indent=4)



def load_module_from_file(file_path):
    with open(file_path) as f:
        file_name = os.path.basename(file_path)
        module_name, _ = os.path.splitext(file_name)
        tmp_module = SourceFileLoader(module_name, file_path).load_module()
    return tmp_module

def tuple_list_to_dialogue(dialogue: List[Tuple]) -> Dialogue:
    for i in range(len(dialogue)):
        turn_tuple = dialogue[i]
        dialogue[i] = DialogueTurn(*turn_tuple)
    return dialogue

def convert_python_files():
    res = []
    
    for (dir_path, dir_names, file_names) in os.walk(DATA_DIR):
        python_files_in_dir = glob.glob(dir_path + '/*.py')

        for python_file_path in python_files_in_dir:
            file_module = load_module_from_file(python_file_path)
            raw_dialogue = file_module.main()
            res += tuple_list_to_dialogue(raw_dialogue)

    return res


def to_soloist_format(turn):
    return {
        "history": [f"user : {turn.user}"],
        "kb": "",
        "belief": f"belief : {turn.belief}",
        "reply": f"system : {turn.system}"
    }

def convert_dialogues_to_soloist(dialogues: List[Dialogue]) -> Tuple[List, List]:
    single_turn = []
    multi_turn = []

    for dialogue in dialogues:
        history = []
        for turn in dialogue:


            single_turn_sample = to_soloist_format(turn)
            history += single_turn_sample['history']
            
            multi_turn_sample = single_turn_sample.copy()
            multi_turn_sample['history'] = [*history]


            # multi_turn_sample = to_soloist_format([*history], turn.system, turn.belief)
            single_turn.append(single_turn_sample)
            multi_turn.append(multi_turn_sample)

            # history.append(turn.system)
            history.append(single_turn_sample['reply'])
    
    return single_turn, multi_turn
    

if __name__ == "__main__":
    # Read Data
    data = convert_python_files()

    # Parametrize


    res = []
    for turn in data:
        try:
            x = fill_samples(turn, train_sampler)
            res.append(to_soloist_format(x))
        except:
            print("FUUUUUUUUUUCK")
    # test_data = parametrize_dialogues(test_data, test_sampler)
    # print(data)

    # # Convert to Soloist
    # train_single, train_multi = convert_dialogues_to_soloist(train_data)
    # test_single, test_multi = convert_dialogues_to_soloist(test_data)

    # # Save To file
    file_name = sys.argv[1]
    
    # print(res)

    save_data(res, f"{file_name}_FINAL.json")
    # # save_data(train_multi, f"{file_name}_train_multi.json")

    # save_data(test_single, f"{file_name}_test_single.json")
    # # save_data(test_multi, f"{file_name}_test_multi.json")
