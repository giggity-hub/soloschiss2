from stuttbard.chatbot.evaluate import parse_beliefstate, create_df, evaluate, resolve_entity, find_all_slots_in_template
import pytest
import pandas as pd
from collections import namedtuple
import re

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


Match = namedtuple("Match", "start stop group")

@pytest.mark.parametrize("test_input, expected", [
    ("slot_df_name", [Match(0, 12, 'slot_df_name')]),
    ('xxx hhh iii mmm slot_df_name sdfasd', [Match(16, 28, 'slot_df_name')]),
    ('slot_entity_phone_number', [Match(0, 24, 'slot_entity_phone_number')]),
    ('slot_entity_phone number', [Match(0, 17, 'slot_entity_phone')]),
    ('xxx slot_entity_a slot_entity_b xxx', [Match(4,17, 'slot_entity_a'), Match(18, 31, 'slot_entity_b')])
])
def test_find_all_slots_in_template(test_input, expected):
    matches = find_all_slots_in_template(test_input)
    assert len(matches) == len(expected)

    for match, match_expected in zip(matches, expected):
        assert match.start() == match_expected.start
        assert match.end() == match_expected.end
        assert match.group() == match_expected.group


# def test_evaluate(domains):
#     sample = {
#         'belief': "domain = restaurant ; query = cuisine == 'italian' ; entity_index = 0",
#         'system': "The name of the place is {entity['name']}"
#     }
#     res = evaluate(sample, domains, None, None)
#     assert res == "The name of the place is Little Ceasars"