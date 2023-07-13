import pytest
from stuttbard.domains.dataframes import load
from stuttbard.domains.sampler import create_sampler

def test_load():
    domains = load()
    assert sorted(domains.keys()) == sorted(['museum', 'restaurant'])

domains = load()

@pytest.mark.parametrize('key, df', domains.items())
def test_no_nan(key, df):
    assert df.isna().sum().sum() == 0


def test_create_sampler():
    sampler = create_sampler()
    sample = sampler['restaurant']['cuisine'].sample()