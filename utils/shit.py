def unroll_belief_state(moped):
    res = []
    for user, system in moped['user_system']:
        res.append((user, system, moped['belief']))

    return res

moped = {
        "belief": "domain = restaurants ; head = 3 ; sortby = rating; cuisine = %(cuisine)s",
        "samplers": {"cuisine": lambda s: s['restaurant']['cuisine']},
        "user_system": [
            ("What are the best %(cuisine)s restaurants in town?",
                "The three highest-rated %(cuisine)s restaurants are: slot_df_name"),
            ("What are the top 3 restaurants that serve %(cuisine)s food",
                "Here are the three highest-rated %(cuisine)s restaurants: slot_df_name"),
            ("Give me the top-3 %(cuisine)s restaurants!",
                "The three highest-rated %(cuisine)s restaurants are: slot_df_name"),
            ("Which %(cuisine)s restaurants have the highest rating?",
                "Here are the three highest rated restaurants: slot_df_name"),
            ("Do you know which %(cuisine)s restaurants are highest rated?",
             "Here are the three highest-rated %(cuisine)s restaurants: slot_df_name"),
            ("What is the best restaurant that serves %(cuisine)s cuisine?",
                "Here are the three highest-rated %(cuisine)s restaurants: slot_df_name"),
        ]
    }

x = unroll_belief_state(moped)
print(x)