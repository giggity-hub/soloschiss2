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


def evaluate(sample, domains, df, entity):
    beliefstate_string = sample['belief']
    bs = parse_beliefstate(beliefstate_string)
    df = create_df(bs, domains, df)
    entity = resolve_entity(bs, df, entity)

    response_template = sample['system']
    res = eval('f"' + response_template.strip() + '"')
    return res
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