def _parse_key_value_string(key_value_string):
    key, value = key_value_string.split('=')
    return (key.lower().strip(), value.lower().strip(),)

def parse_soloist_output(raw_output):
    # The raw output of the model is of the form
    # key = value ; key2 = value2system : systemresponse
    split_at = raw_output.find('system : ')

    belief_state_string = raw_output[:split_at]
    system_response = raw_output[split_at:]
    
    # when there are no assignments in the belief state return empty belief state
    if '=' not in belief_state_string:
        return ({}, system_response,)
    
    key_value_strings = belief_state_string.split(';')
    key_value_tuples = map(_parse_key_value_string, key_value_strings)
    return (dict(key_value_tuples), system_response, )