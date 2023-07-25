def main(parametrize):

    res = []

    # query by area
    res += parametrize({
        "n_repetitions": 2,
        "samplers": {"area": lambda s: s['stairs']['area']},
        "belief": "domain = stairs ; area = %(area)s",
        "user_system": [
            ("Do you know any staeffeles in %(area)s ?", "Here are staeffeles in %(area)s slot_df_name"),
            ("Are there any staeffeles in the %(area)s area?", "Here are staeffeles in %(area)s slot_df_name"),
            ("Please show me some staeffeles in %(area)s", "Here are staeffeles in %(area)s slot_df_name")
        ]
    })

    # Most number of steps
    res+= parametrize({
        "belief": "domain = stairs ; sortby = number_of_steps; entity_index = 0",
        "user_system": [
            ("Which stair has the most number of steps?",
                "With slot_entity_number_of_steps steps, the slot_entity_name has the most steps"),
            ("Show me the stair with the most steps",
                "With slot_entity_number_of_steps steps, the slot_entity_name has the most steps"),
            ("I want to know which stair has the most steps",
                "With slot_entity_number_of_steps steps, the slot_entity_name has the most steps")
        ]
    })

    # res += parametrize({
    #     "user_system": [
    #         "What is the longest stair set in %(area)s?",
            
    #     ]
    # })

    # 5 highest in area
    res+= parametrize({
        "belief": "head = 5 ; sortby = height; area = %(area)s",
        "samplers": {
            'area': lambda s : s['stairs']['area']},
        "user_system": [
            ("Show me the five highest stairs in %(area)s",
                "Here are the five highest stairs in %(area)s. slot_df_name"),
            ("Which stairs in %(area)s belong to the 5 highest?",
                "Here are the five highest stairs in %(area)s. slot_df_name"),
            ("Can you tell me what the five highest stairs are in %(area)s?",
                "Here are the five highest stairs in %(area)s. slot_df_name")
        ]
    })

    

    return res