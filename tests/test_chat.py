from stuttbard.chatbot.evaluate import parse_beliefstate, create_df, evaluate, resolve_entity, find_all_slots_in_template, construct_query
import stuttbard.chatbot.evaluate as ev
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
    df = pd.DataFrame([
        {'cuisine': 'italian', 'name': 'Little Ceasars'},
        {'cuisine': 'french', 'name': 'le baguette'},
        {'cuisine': 'german', 'name': 'zum Wildschwein'}
    ])
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

@pytest.mark.parametrize("test_input, expected", [
    ({'cuisine': 'asian'}, 'cuisine == "asian"'),
    ({'cuisine': 'mexican', 'area': 'Stuttgart-Mitte'}, 'cuisine == "mexican" & area == "Stuttgart-Mitte"'),
    ({'cuisine': 'mexican | asian'}, 'cuisine == "mexican" | "asian"')
])
def test_construct_query(test_input, expected):
    assert construct_query(test_input) == expected


Match = namedtuple("Match", "start end group")

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

@pytest.mark.parametrize("test_input, expected", [
    ('slot_entity_name', 'Little Ceasars'),
    ('slot_entity_cuisine', 'italian'),
    ('slot_df_name', 'Little Ceasars\nle baguette\nzum Wildschwein'),
    ('slot_df_cuisine', 'italian\nfrench\ngerman')
])
def test_render_slot_value(test_input, expected, domains):
    df = domains['restaurant']
    entity = df.iloc[0]

    res =  ev.render_slot_value(test_input, df, entity) 
    assert type(res) == str
    assert res == expected

@pytest.mark.parametrize("test_input, expected", [
    ('The slot_entity_name is open', 'The Little Ceasars is open'),
    ('The cuisine is slot_entity_cuisine', 'The cuisine is italian'),
    ('The names are slot_df_name', 'The names are Little Ceasars\nle baguette\nzum Wildschwein'),
    ('The cuisines are slot_df_cuisine', 'The cuisines are italian\nfrench\ngerman'),
    ('The cuisine of the slot_entity_name is slot_entity_cuisine', 'The cuisine of the Little Ceasars is italian')
])
def test_fill_template_slots(test_input, expected, domains):
    df = domains['restaurant']
    entity = df.iloc[0]

    res = ev.fill_template_slots(test_input, df, entity)
    assert type(res) == str
    assert res == expected


def test_evaluate(domains):
    sample = {
        'belief': "domain = restaurant ; cuisine = italian ; entity_index = 0",
        'system': "The name of the place is slot_entity_name"
    }
    res = evaluate(sample, domains, None, None)
    assert res == "The name of the place is Little Ceasars"


def test_evaluate_with_domain(domains):
    sample = {
        'belief': "entity_index = 0",
        'system': "The name of the place is slot_entity_name"
    }
    df = domains['restaurant']
    res = evaluate(sample, domains, df, None)
    assert res == "The name of the place is Little Ceasars"

def test_evaluate_with_entity(domains):
    sample = {
        'belief': "",
        'system': "The name of the place is slot_entity_name"
    }
    df = domains['restaurant']
    entity = df.iloc[0]
    res = evaluate(sample, domains, df, entity)
    assert res == "The name of the place is Little Ceasars"