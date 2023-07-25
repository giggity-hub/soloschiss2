import pandas as pd
import os
from glob import glob
from typing import Dict
from utils.unique_random import UniqueRandom
from utils.unique_random import get_sampler_split
import random

# We need to use this path, because the working directory path changes based on from where the script is executed
this_dir = os.path.dirname(__file__)
domain_names = ['restaurant', 'museum','stairs']
TRAIN_TEST_SLPIT = 0.8

def load_domains_dict() -> Dict[str , pd.DataFrame]:
    table_paths = [os.path.join(this_dir, domain_name, 'table.csv') for domain_name in domain_names]
    tables = [pd.read_csv(tp, sep=';') for tp in table_paths]
    return dict(zip(domain_names, tables))


def fill_sampler(domains_dict, domain_sampler):
    # Add additional helper methods
    domain_sampler['index'] = UniqueRandom([('first', 0), ('second', 1), ('third', 2), ('fourth', 3), ('fifth', 4), ('last', -1)])
    # Hier kannst du aehnlich wie fuer index einen neuen sampler hinzufuegen
    # Du kannst alle namen aus allen domains in eine liste fuegen indem du alle tabellen joinst 
    # (siehe pandas join oder combine oder whatever weiss gerade nicht genau wie der lachs heisst)
    # und dann die unique values der name column holst

    # domain sampler to sample the domain names randomly
    domain_sampler['domain'] = UniqueRandom(list(domains_dict.keys()))
    
    domain_sampler['number'] = UniqueRandom([('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5), ('six', 6), ('seven', 7), ('eight', 8), ('nine', 9), ('ten', 10)])

    
    """
    pandas join allows not that the two table to join have matching column names
    pandas merge works with "outer" as option but could possibly have duplicates in the name column so 
    it needs extra work
    # domain sampler to sample the names of entities in our dataset
    joined_table = domains_dict[list(domains_dict.keys())[0]]
    for other_table in domains_dict.values():
        # the 
        joined_table = joined_table.merge(other_table, how='outer', on='name')    
    name_list = list(joined_table["name"])
    # this ensures that we have no duplicate of names in our list
    assert(len(set(name_list)) == len(name_list))
    """

    name_list = []
    for other_table in domains_dict.values():
        name_list.extend(list(other_table["name"]))
    # removes duplicates from the name list
    name_list = list(set(name_list))
    domain_sampler['name'] = UniqueRandom(name_list)


    

    domain_sampler['entity_name'] = UniqueRandom([])
    def entity_name_sample():
        rand_name = domain_sampler['name'].sample()
        entity_bs = rand_name
        entity_text = rand_name
        include_domain_name = random.uniform(0, 1) > 0.5
        if include_domain_name:
            rand_domain = domain_sampler['domain'].sample()
            entity_text += ' ' + rand_domain
        return (entity_text, entity_bs, )
    domain_sampler['entity_name'].sample = entity_name_sample

    domain_sampler['entity_index'] = UniqueRandom([])
    def entity_index_sample():
        index_text, index_int = domain_sampler['index'].sample()
        suffix_type = random.choice(['NOTHING', 'ONE', 'RND_DOMAIN'])

        if suffix_type == 'ONE':
            index_text += ' one'
        elif suffix_type == 'RND_DOMAIN':
            random_domain = domain_sampler['domain'].sample()
            index_text += ' ' + random_domain
        
        return (index_text, index_int, )
    domain_sampler['entity_index'].sample = entity_index_sample


    domain_sampler['entity'] = UniqueRandom([])
    def entity_sample():
        entity_type = random.choice(['entity_name', 'entity_index'])
        text_form, bs_form = domain_sampler[entity_type].sample()
        belief_state = f"{entity_type} = {bs_form}"
        return (text_form, belief_state)
    domain_sampler['entity'].sample = entity_sample

    return domain_sampler
    


def load_domain_sampler(domains_dict):
    domain_sampler = {}
    test_sampler = {}
    for domain_name, table in domains_dict.items():
        domain_sampler[domain_name] = {}
        test_sampler[domain_name] = {}
        col_names = list(table.columns.values)
        for col_name in col_names:
            col_values = list(table[col_name].dropna().unique())
            domain_sampler[domain_name][col_name], test_sampler[domain_name][col_name] = get_sampler_split(col_values, TRAIN_TEST_SLPIT)

    domain_sampler = fill_sampler(domains_dict, domain_sampler)
    test_sampler = fill_sampler(domains_dict, test_sampler)

    return domain_sampler, test_sampler

domains_dict = load_domains_dict()
domain_sampler, test_sampler = load_domain_sampler(domains_dict)

