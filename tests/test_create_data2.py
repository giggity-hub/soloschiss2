import pytest
import scripts.create_data as create_data
from scripts.create_data import DialogueTurn, format_dict
from utils.unique_random import UniqueRandom

from domains.domains import load_domain_sampler, domains_dict
train_sampler, test_sampler = load_domain_sampler(domains_dict)

@pytest.mark.parametrize("input", [
    ("user", "system", "belief"),
    ("user", "system")
])
def test_DialogueTurn_success(input):
    dt = DialogueTurn(*input)

@pytest.mark.parametrize("input", [
    ("user", "system", 2343),
    ("user",),
    (True, "sdfsdf")
])
def test_DialogueTurn_fail(input):
    with pytest.raises(Exception):
        dt = DialogueTurn(*input)


@pytest.mark.parametrize("input, expected", [
    ('%(restaurant_name)s', ['restaurant_name']),
    ('What is the number of the %(museum_name)s', ['museum_name']),
    ('sooos %(first_key)s sheeesh %(second_key)s', ['first_key', 'second_key']),
    ('sheesh %(correct_key)s burrr %(faulty_key) sheesh %(faulty key)', ['correct_key'])
])
def test_find_samples(input, expected):
    output = create_data.find_samples(input)
    assert sorted(output) == sorted(expected)

@pytest.mark.parametrize("input, expected", [
    (['index_str'], ['index_str, index_int']),
    (['index_int', 'restaurant_name', 'restaurant_name'], ['index_str, index_int', 'restaurant_name']),
])
def test_get_sampler_keys(input, expected):
    output = create_data.get_sampler_keys(input, train_sampler)
    assert sorted(output) == sorted(expected)


@pytest.mark.parametrize("input", [
    ['index_int', 'index_schmint'], 
    ['restaurant_location'],
    ['stairs_price']
])
def test_get_sampler_keys_exception(input):
    with pytest.raises(Exception):
        output = create_data.get_sampler_keys(input, train_sampler)

@pytest.mark.parametrize("fd", [
    format_dict({'key1': 'value1', 'key2': 'value2'})
])
def test_parametrize(fd):
    turn = DialogueTurn(
        user="Hello %(key1)s",
        system="Hi %(key1)s",
        belief="Bye %(key1)s and %(key2)s" 
    )
    res_turn = create_data.parametrize(turn, fd)
    assert res_turn.user == "user : Hello value1"
    assert res_turn.system == "system : Hi value1"
    assert res_turn.belief == "belief : Bye value1 and value2"


def test_get_samples():
    sampler = UniqueRandom([('World', 1)])
    samplers_dict = {
        "first_param, second_param": sampler
    }

    format_dict = create_data.get_samples(samplers_dict)
    print(format_dict)

    assert format_dict["first_param"] == 'World'
    assert format_dict["second_param"] == 1


def test_fill_samples():
    turn = DialogueTurn(
        user="What is the address of the %(restaurant_name)s",
        system="The address of the %(restaurant_name)s is slot_entity_address",
        belief="entity_name = %(restaurant_name)s" 
    )
    output = create_data.fill_samples(turn, train_sampler)

def test_fill_history_samples():
    histories = [
        [("Tell me about the staeffeles in Stuttgart",
            "In which area would you like to look for staeffeles? i know some in slot_df_area"
                "domain = stairs"),
        ("In the %(stairs_area)s area",
            "Here are some staeffeles in %(stairs_area)s slot_df_name",
                "area = %(stairs_area)s")],
        [("Do you know any good stairs to climb?",
            "In which area would you like to look for staeffeles? i know some in slot_df_area",
                "domain = stairs"),
        ("Show me the ones in %(stairs_area)s",
            "Here are staeffeles in %(stairs_area)s slot_df_name",
                "area = %(stairs_area)s")]
    ]

    histories_filled = create_data.fill_history_samples(histories, train_sampler)