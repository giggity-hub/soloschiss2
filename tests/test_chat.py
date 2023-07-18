from stuttbard.chatbot.evaluate import parse_beliefstate, create_df, evaluate, resolve_entity
import pytest
import pandas as pd

@pytest.mark.parametrize("test_input, expected", [
    ("hello = World ; myval = 2", {'hello': 'World', 'myval': '2'}),
    ("", {}),
    ("domain = restaurant ; query = cuisine == 'italian'", {'domain': 'restaurant', 'query': "cuisine == 'italian'"})
])
def test_parse_beliefstate(test_input, expected):
    assert parse_beliefstate(test_input) == expected

@pytest.fixture
def domains():
    df = pd.DataFrame([{'cuisine': 'italian', 'name': 'Little Ceasars'}])
    domains = {'restaurant': df}
    return domains

def test_create_df(domains):
    bs = parse_beliefstate("domain = restaurant ; query = cuisine == 'italian'")
    df = create_df(bs, domains, None)
    assert df.iloc[0]['name'] == 'Little Ceasars'

def test_resolve_entity(domains):
    bs = parse_beliefstate("domain = restaurant ; query = cuisine == 'italian' ; entity_index = 0")
    df = create_df(bs, domains, None)

    entity = resolve_entity(bs, df, None)
    assert entity['name'] == 'Little Ceasars'


def test_evaluate(domains):
    sample = {
        'belief': "domain = restaurant ; query = cuisine == 'italian' ; entity_index = 0",
        'system': "The name of the place is {entity['name']}"
    }
    res = evaluate(sample, domains, None, None)
    assert res == "The name of the place is Little Ceasars"