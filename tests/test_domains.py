import pytest
from domains.domains import load_domains_dict, load_domain_sampler
import pandas as pd

def test_load_domains():
    domains_dict = load_domains_dict()
    for domain_name, table in domains_dict.items():
        assert type(table) == pd.DataFrame
        assert 'name' in table.columns

def test_domain_sampler_methods():
    domains_dict = load_domains_dict()
    domains_sampler, test_sampler = load_domain_sampler(domains_dict)

    domains_sampler['museum']['about'].sample()
    test_sampler['museum']['about'].sample()

    domains_sampler['restaurant']['cuisine'].sample()
    test_sampler['restaurant']['cuisine'].sample()

def test_load_domain_sampler():
    domains_dict = load_domains_dict()
    domains_sampler, test_sampler = load_domain_sampler(domains_dict)

    random_name = domains_sampler['restaurant']['name'].sample()
    assert type(random_name) == str

    random_name = test_sampler['restaurant']['name'].sample()
    assert type(random_name) == str

def test_sampler_index():
    domains_dict = load_domains_dict()
    domains_sampler, _ = load_domain_sampler(domains_dict)

    index_str, index_int = domains_sampler['index'].sample()
    assert type(index_str) == str
    assert len(index_str) > 0
    assert type(index_int) == int

def test_sampler_name():
    domains_dict = load_domains_dict()
    domains_sampler, _ = load_domain_sampler(domains_dict)

    name = domains_sampler['name'].sample()
    assert type(name) == str
    assert len(name) > 0

def test_sampler_entity_name():
    # The belief state form of the name should be inside the text form
    domains_dict = load_domains_dict()
    domains_sampler, _ = load_domain_sampler(domains_dict)

    name_text, name_bs = domains_sampler['entity_name'].sample()
    assert name_bs in name_text
    print(name_text)
    print(name_bs)
    # assert False

def test_sampler_entity_index():
    # The belief state form of the name should be inside the text form
    domains_dict = load_domains_dict()
    domains_sampler, _ = load_domain_sampler(domains_dict)

    index_str, index_int = domains_sampler['entity_index'].sample()
    assert type(index_str) == str
    assert len(index_str) > 0
    assert type(index_int) == int

    print(index_str)
    print(index_int)
    # assert False

def test_sampler_entity():
    domains_dict = load_domains_dict()
    domains_sampler, _ = load_domain_sampler(domains_dict)

    text_occurence, belief_state = domains_sampler['entity'].sample()
    assert type(text_occurence) == str
    assert type(belief_state) == str
    assert '=' in belief_state

    print(text_occurence)
    print(belief_state)