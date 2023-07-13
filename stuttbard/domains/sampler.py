import random
from typing import Any, Dict, List
import pandas as pd
from stuttbard.domains.dataframes import load

class UniqueRandom:
    def __init__(self, options) -> None:
        # Make sure there are no duplicates in the list
        self.options = list(set(options))
        random.shuffle(self.options)
        self.index = 0
        self.max_index = len(options) -1
    
    def sample(self):
        if self.index >= self.max_index:
            random.shuffle(self.options)
            self.index = 0
        
        value = self.options[self.index]
        self.index += 1
        return value



def create_sampler():
    domains_dict = load()
    sampler = dict({})

    domain_keys = list(domains_dict.keys())
    sampler['keys'] = UniqueRandom(domain_keys)
    sampler['index'] = UniqueRandom([('first', 0), ('second', 1), ('third', 2), ('fourth', 3), ('fifth', 4), ('last', -1)])
    names = []

    for domain_name in domain_keys:
        df = domains_dict[domain_name]
        columns : List[str] = list(df.columns)
        columns_sampler = {col : UniqueRandom(df[col].unique()) for col in columns}
        columns_sampler['columns'] = UniqueRandom(columns)
        sampler[domain_name] = columns_sampler

        names += df['name'].tolist()

    sampler['name'] = UniqueRandom(names)
    return sampler