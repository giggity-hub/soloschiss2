import random
from typing import Any, Dict, List
import pandas as pd
from domains.dataframes import load

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

    for domain_name in domain_keys:
        df = domains_dict[domain_name]
        columns : List[str] = list(df.columns)
        columns_sampler = {col : UniqueRandom(df[col].unique()) for col in columns}
        columns_sampler['columns'] = UniqueRandom(columns)
        sampler[domain_name] = columns_sampler

    return sampler