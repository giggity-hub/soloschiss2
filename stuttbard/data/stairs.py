def main(domain_sampler, parametrize):

    query_by_area = parametrize({
        "n_repetitions": 2,
        "samplers": {"area": domain_sampler['stairs']['area']},
        "belief": "domain = stairs ; area = %(area)s",
        "user_system": [
            ("Do you know any staeffeles in %(area)s ?", "Here are staeffeles in %(area)s slot_df_name"),
            ("Are there any staeffeles in the %(area)s area?", "Here are staeffeles in %(area)s slot_df_name"),
            ("Please show me some staeffeles in %(area)s", "Here are staeffeles in %(area)s slot_df_name")
        ]
    })

    ask_for_attribute_by_name = parametrize({
        "n_repetitions": 2,
        "samplers": {"stairs_name": domain_sampler['stairs']['name']},
        "belief": "entity_name = %(stairs_name)s",
        "user_system": [
            # ask for named_after
            ("Who was the %(stairs_name)s named after?", 
                "The slot_entity_name was named after slot_entity_named_after"),
            ("Who gave the %(stairs_name)s it's name?", 
                "The slot_entity_name was named after slot_entity_named_after"),
            # Ask for number_of_steps
            ("How many steps does the the %(stairs_name)s have?",
                "The slot_entity_name has slot_entity_number_of_steps stairs"),
            ("What's the stair count for the %(stairs_name)s?",
                "The slot_entity_name has slot_entity_number_of_steps stairs"),
            # Ask for length
            ("How long is the %(stairs_name)s ?",
                "The slot_entity_name is slot_entity_length meters long"),
            ("What's the length of the %(stairs_name)s ?",
                "The slot_entity_name is slot_entity_length meters long"),
            # Ask for height
            ("How high is the %(stairs_name)s ?",
                "The slot_entity_name is slot_entity_height meters high"),
            ("What's the height of the %(stairs_name)s ?",
                "The slot_entity_name is slot_entity_height meters high"),
            # Ask for area
            ("Which area of Stuttgart is the %(stairs_name)s in?",
                "The slot_entity_name is in slot_entity_area"),
            ("In which part of town is the %(stairs_name)s located?",
                "The slot_entity_name is in slot_entity_area")
        ]
    })

    ask_for_maximum_values = [
        {"user": "Which staeffele has the most steps?",
        "belief": "domain = stairs ; sortby = number_of_steps ; entity_index= 0",
        "system": "With slot_entity_number_of_steps steps, the slot_entity_name has the most steps"},
        {"user": "Which is the highest staeffele in Stuttgart?",
        "belief": "domain = stairs ; sortby = height ; entity_index= 0",
        "system": "With a height of slot_entity_height meters, the slot_entity_name is the highest"},
        {"user": "Which is the longest staeffele in Stuttgart?",
        "belief": "domain = stairs ; sortby = length ; entity_index= 0",
        "system": "With a length of slot_entity_length meters, the slot_entity_name is the longest"}
    ]

    return [*query_by_area, *ask_for_attribute_by_name, *ask_for_maximum_values]