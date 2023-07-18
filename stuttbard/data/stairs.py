def main(domain_sampler, parametrize):

    query_by_area = parametrize({
        "n_repetitions": 2,
        "samplers": {"area": domain_sampler['stairs']['area']},
        "belief": "domain = stairs ; query = area == '%(area)s'",
        "user_system": [
            ("Do you know any staeffeles in %(area)s ?", "Here are staeffeles in %(area)s {templates.list(df['name'])}"),
            ("Are there any staeffeles in the %(area)s area?", "Here are staeffeles in %(area)s {templates.list(df['name'])}"),
            ("Please show me some staeffeles in %(area)s", "Here are staeffeles in %(area)s {templates.list(df['name'])}")
        ]
    })

    ask_for_attribute_by_name = parametrize({
        "n_repetitions": 2,
        "samplers": {"stairs_name": domain_sampler['stairs']['name']},
        "belief": "entity_name = %(stairs_name)s",
        "user_system": [
            # ask for named_after
            ("Who was the %(stairs_name)s named after?", 
                "The {entity['name']} was named after {entity['named_after']}. {entity['named_after_description']}"),
            ("Who gave the %(stairs_name)s it's name?", 
                "The {entity['name']} was named after {entity['named_after']}. {entity['named_after_description']}"),
            # Ask for number_of_steps
            ("How many steps does the the %(stairs_name)s have?",
                "The {entity['name']} has {entity['number_of_steps']} stairs"),
            ("What's the stair count for the %(stairs_name)s?",
                "The {entity['name']} has {entity['number_of_steps']} stairs")
            # Ask for length
            ("How long is the %(stairs_name)s ?",
                "The {entity['name']} is {entity['length']} meters long"),
            ("What's the length of the %(stairs_name)s ?",
                "The {entity['name']} is {entity['length']} meters long"),
            # Ask for height
            ("How high is the %(stairs_name)s ?",
                "The {entity['name']} is {entity['height']} meters high"),
            ("What's the height of the %(stairs_name)s ?",
                "The {entity['name']} is {entity['height']} meters high"),
            # Ask for area
            ("Which area of Stuttgart is the %(stairs_name)s in?",
                "The {entity['name']} is in {entity['area']}"),
            ("In which part of town is the %(stairs_name)s located?",
                "The {entity['name']} is in {entity['area']}")
        ]
    })

    ask_for_maximum_values = [
        {"user": "Which staeffele has the most steps?"
        "belief": "domain = stairs ; sortby = number_of_steps ; entity_index= 0"
        "system": "With {entity['number_of_steps']} steps, the {entity['name']} has the most steps"},
        {"user": "Which is the highest staeffele in Stuttgart?"
        "belief": "domain = stairs ; sortby = height ; entity_index= 0"
        "system": "With a height of {entity['height']} meters, the {entity['name']} is the highest"},
        {"user": "Which is the longest staeffele in Stuttgart?"
        "belief": "domain = stairs ; sortby = length ; entity_index= 0"
        "system": "With a length of {entity['length']} meters, the {entity['name']} is the longest"}
    ]
