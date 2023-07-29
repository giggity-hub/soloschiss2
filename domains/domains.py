import pandas as pd
import os
from glob import glob
from typing import Dict
from utils.unique_random import UniqueRandom
from utils.unique_random import get_sampler_split
import random
from sklearn.model_selection import train_test_split

# We need to use this path, because the working directory path changes based on from where the script is executed
this_dir = os.path.dirname(__file__)
domain_names = ['restaurant', 'museum','stairs']
TRAIN_SIZE = 0.75

def load_domains_dict() -> Dict[str , pd.DataFrame]:
    table_paths = [os.path.join(this_dir, domain_name, 'table.csv') for domain_name in domain_names]
    tables = [pd.read_csv(tp, sep=';') for tp in table_paths]
    return dict(zip(domain_names, tables))


def fill_sampler(domains_dict, domain_sampler):
    domain_sampler['index_str, index_int'] = UniqueRandom([('first', 1), ('second', 2), ('third', 3), ('fourth', 4), ('fifth', 5), ('last', -1)])

    # domain_sampler['domain'] = UniqueRandom(list(domains_dict.keys()))
    
    domain_sampler['number_str, number_int'] = UniqueRandom([('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5), ('six', 6), ('seven', 7), ('eight', 8), ('nine', 9), ('ten', 10)])

    return domain_sampler

description = {
    'restaurant': ['name', 'house_number', 'street', 'area', 'postal_code', 'phone_number', 'website', 'url', 'rating', 'price_level', 'address', 'wheelchair_access', 'cuisine'],
    'museum': ['about', 'about_specific', 'for_children', 'name', 'house_number', 'street', 'area', 'phone_number', 'website', 'url', 'rating', 'address', 'wheelchair_access'],
    'stairs': ['name', 'area', 'number_of_steps', 'length', 'height', 'named_after']
}

def load_domain_sampler(domains_dict):
    train_sampler = {}
    test_sampler = {}
    for domain_name, table in domains_dict.items():
        train_sampler[domain_name] = {}
        test_sampler[domain_name] = {}
        col_names = description[domain_name]
        for col_name in col_names:
            col_values = list(table[col_name].dropna().unique())
            try:
                col_values_train, col_values_test = train_test_split(col_values, train_size=TRAIN_SIZE)
            except:
                col_values_train = [*col_values]
                col_values_test = [*col_values]
            key = f'{domain_name}_{col_name}'
            train_sampler[key] = UniqueRandom(col_values_train)
            test_sampler[key] = UniqueRandom(col_values_test)

    train_sampler = fill_sampler(domains_dict, train_sampler)
    test_sampler = fill_sampler(domains_dict, test_sampler)

    return train_sampler, test_sampler

domains_dict = load_domains_dict()
domain_sampler, test_sampler = load_domain_sampler(domains_dict)

