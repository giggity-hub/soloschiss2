import re
from typing import Dict, List
import pandas as pd


def parse_beliefstate(beliefstate_string: str) -> dict:
    """Parse a belief state string into a dictionary. 
    parse_beliefstate("name = Hatori ; cuisine = chinese") = {'name': 'Hatori', 'cuisine': 'chinese'}

    Args:
        beliefstate_string (str): The belief state string from the model

    Returns:
        dict: The parsed belief state dictionary
    """
    if '=' not in beliefstate_string:
        return {}
    
    code_blocks = beliefstate_string.split(";")
    code_blocks = [cb.strip() for cb in code_blocks ]
    res = {}
    for cb in code_blocks:
        key, val = cb.split("=",1)
        key = key.strip()
        val = val.strip()
        res[key] = val
    return res


SPECIAL_WORDS = ['sortby', 'head', 'domain', 'entity_name', 'entity_index']
OR_CHARACTER = ' or '

def construct_query(bs: dict) -> str:
    """Constructs a pandas df query string from a belief state.
    It is assumed, that all values that are not reserved keywords are mean to be queries

    construct_query({'cuisine': 'chinese | japanese', 'area': 'Stuttgart-Mitte'}) 
    => "cuisine == 'chinese' | 'japanese' & area == 'Stuttgart-Mitte'"

    Args:
        bs (dict): A belief state dictionary

    Returns:
        str: A pandas dataframe query string
    """
    constraints = []
    for key, val in bs.items():
        if key in SPECIAL_WORDS:
            continue
        options = val.split(OR_CHARACTER)
        options = [f'"{opt.strip()}"' for opt in options]
        expression = f'{key} == {" | ".join(options)}'
        constraints.append(expression)

    if len(constraints) == 0:
        return None
    else:
        return " & ".join(constraints)
    

def create_df(bs: dict, domains: Dict[str, pd.DataFrame], df: pd.DataFrame) -> pd.DataFrame:
    """This function determines which dataframe the user is talking about by evaluating the belief state.
    If the user does not change or constrain the current dataframe This function does nothing.


    Args:
        bs (dict): A Belief State Dictionary
        domains (Dict[str, pd.DataFrame]): The domains Dictionary
        df (pd.DataFrame): The selected dataframe before evluation of the belief state

    Returns:
        pd.DataFrame: The selected dataframe after evaluating the belief state
    """
    bs['query'] = construct_query(bs)
    if 'domain' in bs and bs['domain'] is not None:
        df = domains[bs['domain']]
    if 'query' in bs and bs['query'] is not None:
        df = df.query(bs['query'])
    if 'head' in bs and bs['head'] is not None:
        df = df.head(int(bs['head']))
    if 'sortby' in bs and bs['sortby'] is not None:
        df = df.sort_values(by=bs['sortby'])

    return df

def resolve_entity(bs: dict, df: pd.DataFrame, entity : pd.Series) -> pd.Series:
    """This function updates the selected entity based on the belief state.
    A new entity will be selected if either entity_index or entity_name are present in the belief state.

    Args:
        bs (dict): _description_
        df (pd.DataFrame): _description_
        entity (pd.Series): _description_

    Returns:
        pd.Series: _description_
    """
    # if domain in bs then entity = first

    if 'entity_index' in bs:
        index = int(bs['entity_index'])
        if index > 0:
            index  -= 1
        return df.iloc[index]

    elif 'entity_name' in bs:
        return df[df['name'].str.contains(bs['entity_name'])].iloc[0]
    return entity

def render_df(df):
    return df.to_string()

def render_entity_value(entity, column):
    return str(entity[column])

def render_column(df, column):
    return '\n' + '\n'.join(list(df[column].unique()))

def render_slot_value(matched_slot, df, entity):
    values = matched_slot.split('_', maxsplit=2)

    # extract column name from the placeholder variable
    column = values[2] if len(values) == 3 else None

    if values[1] == 'df' and not column:
        return render_df(df)
    # if the column is specified, lists its unique values
    elif values[1] == 'df' and column:
        return render_column(df, column)
    # returns the value of the specific entity in this column
    elif values[1] == 'entity' and column:
        return render_entity_value(entity, column)

def find_all_slots_in_template(template_string: str):
    """Find all slots in a system response string.
    Slots are indicated by slot_df_xxx or slot_entity_xxx

    find_all_slots_in_template("The address is slot_entity_address")

    Args:
        template_string (str): _description_

    Returns:
        List[re.Match]: _description_
    """
    pattern = 'slot_(entity|df)[a-z_]*'
    matches = [m for m in re.finditer(pattern, template_string)]
    return matches

def fill_template_slots(template_string, df, entity):
    matches = find_all_slots_in_template(template_string)
    print(f"matches: {matches}")
    for match in matches:
        matched_slot = match.group()
        slot_value = render_slot_value(matched_slot, df, entity)
        # if there's no information about the requested attribute, give up
        if slot_value == "None":
            template_string = "Sorry, I don't have this information."
            break
        template_string = template_string.replace(matched_slot, slot_value)
    
    return template_string


def evaluate(sample, domains, df, entity):
    beliefstate_string = sample['belief']
    bs = parse_beliefstate(beliefstate_string)
    print(f"belief_state: {bs}")
    
    df = create_df(bs, domains, df)
    
    print(f"df: {df.head() if df is not None else df}")
    entity = resolve_entity(bs, df, entity)
    print(f"entity: {entity}")

    response_template = sample['system']
    res = fill_template_slots(response_template, df, entity)
    return res, df, entity
