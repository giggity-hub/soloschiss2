import pytest
from domains.domains import load_domains_dict, load_domain_sampler
import pandas as pd

def test_load_domains():
    domains_dict = load_domains_dict()
    for domain_name, table in domains_dict.items():
        assert type(table) == pd.DataFrame
        assert 'name' in table.columns

def test_load_domain_sampler():
    domains_dict = load_domains_dict()
    domains_sampler = load_domain_sampler(domains_dict)

    random_name = domains_sampler['view']['name'].sample()
    assert type(random_name) == str