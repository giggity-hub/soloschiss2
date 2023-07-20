import re

def parse_beliefstate(beliefstate_string: str):
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
OR_CHARACTER = '|'

def construct_query(bs):
    # Assume that every key value where key is not a special word is a query constraint
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
    

def create_df(bs, domains, df):
    bs['query'] = construct_query(bs)
    if 'domain' in bs and bs['domain'] is not None:
        df = domains[bs['domain']]
    if 'query' in bs and bs['query'] is not None:
        df = df.query(bs['query'])
    if 'head' in bs and bs['head'] is not None:
        df = df.head(bs['head'])
    if 'sortby' in bs and bs['sortby'] is not None:
        df = df.sortby(bs['sortby'])

    return df

def resolve_entity(bs, df, entity):
    if 'entity_index' in bs:
        return df.iloc[int(bs['entity_index'])]
    elif 'entity_name' in bs:
        return df[df['name'].str.contains(bs['entity_name'])].iloc[0]
    return entity

def render_df(df):
    return df.to_string()

def render_entity_value(entity, column):
    return str(entity[column])

def render_column(df, column):
    return '\n'.join(df[column].tolist())

def render_slot_value(matched_slot, df, entity):
    values = matched_slot.split('_', maxsplit=2)

    column = values[2] if len(values) == 3 else None

    if values[1] == 'df' and not column:
        return render_df(df)
    elif values[1] == 'df' and column:
        return render_column(df, column)
    elif values[1] == 'entity' and column:
        return render_entity_value(entity, column)

def find_all_slots_in_template(template_string):
    pattern = 'slot_(entity|df)[a-z_]*'
    matches = [m for m in re.finditer(pattern, template_string)]
    return matches

def fill_template_slots(template_string, df, entity):
    matches = find_all_slots_in_template(template_string)
    print(f"matches: {matches}")
    for match in matches:
        matched_slot = match.group()
        slot_value = render_slot_value(matched_slot, df, entity)
        template_string = template_string.replace(matched_slot, slot_value)
    
    return template_string


def evaluate(sample, domains, df, entity):
    beliefstate_string = sample['belief']
    bs = parse_beliefstate(beliefstate_string)
    print(f"belief_state: {bs}")
    
    df = create_df(bs, domains, df)
    print(f"df: {df.head()}")
    entity = resolve_entity(bs, df, entity)
    print(f"entity: {entity}")

    response_template = sample['system']
    res = fill_template_slots(response_template, df, entity)
    return res, df, entity
