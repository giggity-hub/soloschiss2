import pandas as pd
import os
from glob import glob
from typing import Dict
from utils.unique_random import UniqueRandom

# We need to use this path, because the working directory path changes based on from where the script is executed
this_dir = os.path.dirname(__file__)
domain_names = ['restaurant', 'museum','stairs']

def load_domains_dict() -> Dict[str , pd.DataFrame]:
    table_paths = [os.path.join(this_dir, domain_name, 'table.csv') for domain_name in domain_names]
    tables = [pd.read_csv(tp, sep=';') for tp in table_paths]
    return dict(zip(domain_names, tables))


def load_domain_sampler(domains_dict):
    domain_sampler = {}
    for domain_name, table in domains_dict.items():
        domain_sampler[domain_name] = {}
        col_names = list(table.columns.values)
        for col_name in col_names:
            col_values = list(table[col_name].dropna().unique())
            domain_sampler[domain_name][col_name] = UniqueRandom(col_values)

    # Add additional helper methods
    domain_sampler['index'] = UniqueRandom([('first', 0), ('second', 1), ('third', 2), ('fourth', 3), ('fifth', 4), ('last', -1)])
    return domain_sampler

domains_dict = load_domains_dict()
domain_sampler = load_domain_sampler(domains_dict)