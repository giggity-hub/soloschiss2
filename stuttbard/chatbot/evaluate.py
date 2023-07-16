def parse_beliefstate(beliefstate_string: str):
    code_blocks = belief_string.split(";")
    code_blocks = [cb.strip() for cb in code_blocks ]

    return code_blocks


def action(belief_dict):
    return "sheeesh"


def create_df(locals, prev):
    if domain:
        df = domains[domain]
    if query:
        df = df.query(query)
    if head:
        df = df.head(head)
    if sortby:
        df = df.sortby(sortby)
    if cols:
        df = df[cols]

    return df

# df = domains[domain_name].query(query).head(head).sortby(by, )
# 
def evaluate(beliefstate_string: str, prev):
    belief_dict = parse_beliefstate(beliefstate_string)
    # 
    # 

    # split the sections
    pre_df, post_df = beliefstate_string.split("variables : ")

    # Run code bevor the df exists
    for code in get_codes(pre_df):
        try:
            exec(code)
        except:
            print("Failed to execute: " + code)
    
    df = create_df(locals(), df)

    # Run code after the df exists
    for code in get_codes(post_df):
        try:
            exec(code)
        except:
            print("Failed to execute: " + code)

    res = eval("f'" + belief_string.strip() + "'")
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