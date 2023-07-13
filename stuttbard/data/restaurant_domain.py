def main(domain_sampler, parametrize):

    query_by_cuisine = parametrize({
        "n_repetitions": 2,
        "samplers": {"cuisine": domain_sampler['restaurant']['cuisine']},
        "belief": "df = domains['restaurant'].query('cuisine == \"%(cuisine)s\"') ; names = df['name'].tolist()",
        "user_system": [
            ("I want to eat %(cuisine)s food", "Here are some %(cuisine)s restaurants {templates.list(names)}"),
            ("I'd like to get a %(cuisine)s meal", "These restaurants serve %(cuisine)s meals {templates.list(names)}"),
            ("Where can i get some %(cuisine)s food?", "You can get %(cuisine)s food at these restaurants {templates.list(names)}"),
            ("I want to eat %(cuisine)s", "Here are some %(cuisine)s restaurants {templates.list(names)}"),
            ("give me %(cuisine)s restaurants", "Here are %(cuisine)s restaurants {templates.list(names)}"),
            ("List %(cuisine)s restaurants", "Here is a list of %(cuisine)s restaurants {templates.list(names)}"),
        ]
    })

    query_domain = parametrize({
        "belief": "df = domains['restaurant'] ; cuisines = df['cuisine'].unique()",
        "user_system": [
            ("I want to go to a restaurant", "What kind of restaurants do you like? {templates.list(cuisines)}"),
            ("I want to eat some food", "What type of food do you want to eat? {templates.list(cuisines)}"),
            ("Do you know any restaurants?", "Sure. Which cuisines should the restaurant serve? {templates.list(cuisines)}"),
            ("Where can i grab something to eat?", "What cuisines are you interested in? {templates.list(cuisines)}"),
            ("Are there any restaurants you know of?", "Yes! I know restaurants that serve the following cuisines {templates.list(cuisines)}"),
            ("I'd like to eat something", "What kind of food would you like to eat? {templates.list(cuisines)}")
        ]
    })

    query_by_2_cuisines = parametrize({
        "n_repetitions": 2,
        "belief": "df = domains['restaurant'].query('cuisine == \"%(cuisine1)s\" | cuisine == \"%(cuisine2)s\"') ; names = df['name'].tolist()",
        "samplers": {
            "cuisine1": domain_sampler['restaurant']['cuisine'],
            "cuisine2": domain_sampler['restaurant']['cuisine']},
        "user_system": [
            ("Do you know any restaurants that are either %(cuisine1)s or %(cuisine2)s", 
                "Here are restaurants that fit your description {templates.list(names)}"),
            ("I like %(cuisine1)s and %(cuisine2)s food",
                "Then you should like these restaurants {templates.list(names)}"),
            ("I want food that is  %(cuisine1)s or %(cuisine2)s",
                "Then you should like these restaurants {templates.list(names)}")
        ]
    })

    return [*query_by_cuisine, *query_domain, *query_by_2_cuisines]
