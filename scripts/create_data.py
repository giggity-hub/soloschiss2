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
from collections import namedtuple

from domains.domains import load_domain_sampler
from domains.domains import domains_dict
import re
from typing import List, TypeAlias, Tuple

from scripts.parametrize import parametrize_dialogues
from scripts.types import Dialogue, DialogueTurn

DATA_DIR = './stuttbard/data_multiturn'
OUT_DIR = './data'




train_sampler, test_sampler = load_domain_sampler(domains_dict)



def save_data(data, out_file):
    out_path = os.path.join(OUT_DIR, out_file)
    with open(out_path, 'w+') as f:
        json.dump(data, f, indent=4)


def to_soloist_format(dt: DialogueTurn):
    soloist_dict = {
        "history": [dt.user],
        "belief": dt.belief,
        "kb": "",
        "reply": dt.system
    }
    return soloist_dict


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
    train_data = []
    test_data = []
    
    for (dir_path, dir_names, file_names) in os.walk(DATA_DIR):
        python_files_in_dir = glob.glob(dir_path + '/*.py')

        for python_file_path in python_files_in_dir:
            file_module = load_module_from_file(python_file_path)
            raw_dialogues = file_module.main()
            dialogues = [tuple_list_to_dialogue(d) for d in raw_dialogues]

            train_split, test_split = train_test_split(dialogues, test_size=0.25)
            train_data += train_split
            test_data += test_split

    return train_data, test_data


def to_soloist_format(history, belief, reply):
    return {
        "history:": history,
        "kb": "",
        "belief": f"belief : {belief}",
        "reply": f"system : {reply}"
    }

def convert_dialogues_to_soloist(dialogues: List[Dialogue]) -> Tuple[List, List]:
    single_turn = []
    multi_turn = []

    history = []
    for dialogue in dialogues:
        for turn in dialogue:
            history.append(turn.user)

            single_turn_sample = to_soloist_format([turn.user], turn.system, turn.belief)
            multi_turn_sample = to_soloist_format([*history], turn.system, turn.belief)
            single_turn.append(single_turn_sample)
            multi_turn.append(multi_turn_sample)

            history.append(turn.system)
    
    return single_turn, multi_turn
    

if __name__ == "__main__":
    # Read Data
    train_data, test_data = convert_python_files()

    # Parametrize
    train_data = parametrize_dialogues(train_data, train_sampler)
    test_data = parametrize_dialogues(test_data, test_sampler)

    # Convert to Soloist
    train_single, train_multi = convert_dialogues_to_soloist(train_data)
    test_single, test_multi = convert_dialogues_to_soloist(test_data)

    # Save To file
    file_name = sys.argv[1]
    
    save_data(train_single, f"{file_name}_train_single.json")
    save_data(train_multi, f"{file_name}_train_multi.json")

    save_data(test_single, f"{file_name}_test_single.json")
    save_data(test_multi, f"{file_name}_test_multi.json")
