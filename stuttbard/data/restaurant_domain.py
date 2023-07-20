def main(domain_sampler, parametrize):

    query_by_cuisine = parametrize({
        "n_repetitions": 2,
        "samplers": {"cuisine": domain_sampler['restaurant']['cuisine']},
        "belief": "domain = restaurant ; cuisine = %(cuisine)s",
        "user_system": [
            ("I want to eat %(cuisine)s food", "Here are some %(cuisine)s restaurants slot_df_names"),
            ("I'd like to get a %(cuisine)s meal", "These restaurants serve %(cuisine)s meals slot_df_names"),
            ("Where can i get some %(cuisine)s food?", "You can get %(cuisine)s food at these restaurants slot_df_names"),
            ("I want to eat %(cuisine)s", "Here are some %(cuisine)s restaurants slot_df_names"),
            ("give me %(cuisine)s restaurants", "Here are %(cuisine)s restaurants slot_df_names"),
            ("List %(cuisine)s restaurants", "Here is a list of %(cuisine)s restaurants slot_df_names"),
        ]
    })

    query_domain = parametrize({
        "n_repetitions": 1,
        "belief": "domain = restaurant",
        "user_system": [
            ("I want to go to a restaurant", "What kind of restaurants do you like? slot_df_cuisine"),
            ("I want to eat some food", "What type of food do you want to eat? slot_df_cuisine"),
            ("Do you know any restaurants?", "Sure. Which cuisines should the restaurant serve? slot_df_cuisine"),
            ("Where can i grab something to eat?", "What cuisines are you interested in? slot_df_cuisine"),
            ("Are there any restaurants you know of?", "Yes! I know restaurants that serve the following cuisines slot_df_cuisine"),
            ("I'd like to eat something", "What kind of food would you like to eat? slot_df_cuisine")
        ]
    })

    query_by_2_cuisines = parametrize({
        "n_repetitions": 2,
        "belief": "domain = restaurant ; cuisine = %(cuisine1)s | %(cuisine2)s",
        "samplers": {
            "cuisine1": domain_sampler['restaurant']['cuisine'],
            "cuisine2": domain_sampler['restaurant']['cuisine']},
        "user_system": [
            ("Do you know any restaurants that are either %(cuisine1)s or %(cuisine2)s", 
                "Here are restaurants that fit your description slot_df_names"),
            ("I like %(cuisine1)s and %(cuisine2)s food",
                "Then you should like these restaurants slot_df_names"),
            ("I want food that is  %(cuisine1)s or %(cuisine2)s",
                "Then you should like these restaurants slot_df_names")
        ]
    })

    return [*query_by_cuisine, *query_domain, *query_by_2_cuisines]
