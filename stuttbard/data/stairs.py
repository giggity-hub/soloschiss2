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
            ("Please show me some staeffeles in %(area)s", "Here are staeffeles in %(area)s slot_df_name"),
            ("I want to go to a staeffele in %(area)s", "Here are staeffeles in %(area)s slot_df_name")
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
                "With slot_entity_number_of_steps steps, the slot_entity_name has the most steps"),
            ("Tell me which staeffeles has the most steps",
                "With slot_entity_number_of_steps steps, the slot_entity_name has the most steps")
        ]
    })

    res += parametrize({
        "belief": ""
    })


    # 5 highest in area
    res+= parametrize({
        "belief": "domain = stairs ; head = 5 ; sortby = height; area = %(area)s",
        "samplers": {
            'area': lambda s : s['stairs']['area']},
        "user_system": [
            ("Show me the five highest stairs in %(area)s",
                "Here are the five highest stairs in %(area)s. slot_df_name"),
            ("Which stairs in %(area)s belong to the 5 highest?",
                "Here are the five highest stairs in %(area)s. slot_df_name"),
            ("Can you tell me what the five highest stairs are in %(area)s?",
                "Here are the five highest stairs in %(area)s. slot_df_name"),
            ("I want to know what the five highest staeffeles in %(area)s are",
                "Here are the five highest stairs in %(area)s. slot_df_name"),
        ]
    })


    res += parametrize({
        'samplers': {
            'name': lambda s : s['stairs']['name']
        },
        'belief': "entity_name = %(name)s",
        "user_system": [
            ("How high is the %(name)s ?",
                "The slot_entity_name has a height of slot_entity_height"),
            ("What is the height of the %(name)s ?",
                "The slot_entity_name has a height of slot_entity_height"),
            ("How many steps does the %(name)s have?",
                "The slot_entity_name has slot_entity_number_of_steps steps"),
            ("Wha is the number of steps of the %(name)s?",
                "The slot_entity_name has slot_entity_number_of_steps steps")
            ("Tell me the length of the %(name)s",
                "The slot_entity_name has a length of slot_entity_length"),
            ("How long is the %(name)s?",
                "The slot_entity_name has a length of slot_entity_height"),
            ("Who was the %(name)s named after?",
                "The slot_entity_name was named after slot_entity_named_after"),
            ("How did the %(name)s come to its name?",
                "The slot_entity_name was named after slot_entity_named_after"),
            ("What area is the %(name)s in?",
                "The slot_entity_name is in the slot_entity_area area"),
            ("In which part of town is the %(name)s in?",
                "The slot_entity_name is in the slot_entity_area area")
        ]
    })

    res += parametrize({
        'samplers': {
            'index_text, index_int': lambda s : s['index']
        },
        'belief': "entity_index = %(index_int)s",
        "user_system": [
            ("Tell me the height of the %(index_text)s one please",
                "The slot_entity_name has a height of slot_entity_height"),
            ("How high is the %(index_text)s of those?",
                "The slot_entity_name has a height of slot_entity_height"),
            # Number of steps
            ("Look up how many steps the %(index_text)s set of stairs has please",
                "The slot_entity_name has slot_entity_number_of_steps steps"),
            ("Do you know how many steps the %(index_text)s one has?",
                "The slot_entity_name has slot_entity_number_of_steps steps")
            # Length
            ("What's the length of the %(index_text)s one?",
                "The slot_entity_name has a length of slot_entity_length"),
            ("Tell me how long the %(index_text)s one is please",
                "The slot_entity_name has a length of slot_entity_height"),
            ("I want to know who the %(index_text)s of those was named after",
                "The slot_entity_name was named after slot_entity_named_after"),
            ("Do you know who the %(index_text)s was named after?",
                "The slot_entity_name was named after slot_entity_named_after"),
            ("In which area can i find the %(index_text)s one?",
                "The slot_entity_name is in the slot_entity_area area"),
            ("Which area of Stuttgart is the %(index_text)s in?",
                "The slot_entity_name is in the slot_entity_area area")
        ]

    })

    res += parametrize({
        'samplers': {
            'index_text, index_int': lambda s : s['index']
        },
        'belief': "",
        "user_system": [
            ("Tell me it's height",
                "The slot_entity_name has a height of slot_entity_height"),
            ("How high is it?",
                "The slot_entity_name has a height of slot_entity_height"),
            # Number of steps
            ("How many steps does it have?",
                "The slot_entity_name has slot_entity_number_of_steps steps"),
            ("Can you tell me the number of steps of that one?",
                "The slot_entity_name has slot_entity_number_of_steps steps")
            # Length
            ("What's it's length?",
                "The slot_entity_name has a length of slot_entity_length"),
            ("Tell me how long it is",
                "The slot_entity_name has a length of slot_entity_height"),
            ("Who was that stair set named after?",
                "The slot_entity_name was named after slot_entity_named_after"),
            ("Who gave it it's name?",
                "The slot_entity_name was named after slot_entity_named_after"),
            ("In what part of town is it?",
                "The slot_entity_name is in the slot_entity_area area"),
            ("Which part of town is it in?",
                "The slot_entity_name is in the slot_entity_area area")
        ]

    })
    

    return res