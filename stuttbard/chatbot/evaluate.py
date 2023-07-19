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


def action(belief_dict):
    return "sheeesh"


def create_df(bs, domains, df):
    if 'domain' in bs:
        df = domains[bs['domain']]
    if 'query' in bs:
        df = df.query(bs['query'])
    if 'head' in bs:
        df = df.head(bs['head'])
    if 'sortby' in bs:
        df = df.sortby(bs['sortby'])

    return df

def resolve_entity(bs, df, entity):
    if 'entity_index' in bs:
        return df.iloc[int(bs['entity_index'])]
    elif 'entity_name' in bs:
        return df[df['name'] == bs['entity_name']].iloc[0]
    return entity



def render_entity_value():
    pass

def render_column():
    pass

def find_all_slots_in_template(template_string):
    # define this pattern
    pattern = ''
    matches = [m for m in re.finditer(pattern, template_string)]
    return matches

def fill_template_slots(template_string, df, entity):
    matches = find_all_slots_in_template()
    pass
    # 1.) find all substrings of the form slot_df_xxxx or slot_entity_xxx
    # column names may also include underscores but never a space
    # slot_df_xxx means that column xxx should be displayed
    # slot_entity_xxx means that attribute xxx of the entity should be displayed
    # 2.) Once you have all the matches replace the slots in the string with correct values
    # for columns (slot_df_xxx) use render_column() and for entity values (slot_entity_xxx) use render_entity_value()


def evaluate(sample, domains, df, entity):
    beliefstate_string = sample['belief']
    bs = parse_beliefstate(beliefstate_string)
    df = create_df(bs, domains, df)
    entity = resolve_entity(bs, df, entity)

    response_template = sample['system']
    res = fill_template_slots(response_template, df, entity)
    return res





    

# mentions = df
# mentions

# entity0 : df[df['name']=='Stefan']
# df.iloc[0]

# the phone number of the entity0['name'] 

# entity1 = 

# What is the phone number of the first one? entity = df. entity0 =  entity1 = df.iloc[0]
# cols = [phone_number]

# What is its address? 
# entity0['address'] ; cols = ['address']

# What is the telephone number of the Hatori?
# number = domains['restaurant'].query()
# hatori = 

# What are their ratings?
# the rating of the 


def soos():
    x = 'asdfd'
    print(locals())

if __name__ == "__main__":
    evaluate("domain = 'restaurant', ")