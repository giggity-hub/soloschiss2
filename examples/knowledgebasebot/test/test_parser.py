import pytest
from chatbot import parse_soloist_output

def test_parse_soloist_output_without_belief():
    belief_state_dict, system_response = parse_soloist_output('system : action_do_something')

    assert belief_state_dict == {}
    assert system_response == 'system : action_do_something'

def test_parse_soloist_output_with_belief():
    belief_state_dict, system_response = parse_soloist_output('hello = world ; key = valuesystem : action_do_something')

    assert belief_state_dict == {"hello": "world", "key": "value"}
    assert system_response == 'system : action_do_something'