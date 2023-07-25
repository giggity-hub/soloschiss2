def main(domain_sampler, parametrize):

    query_by_type = parametrize({
        "n_repetitions": 2,
        "samplers": {"topic": domain_sampler['museum']['about']},
        "belief": "domain = museum ; about = %(topic)s",
        "user_system": [
            ("I want to visit a %(topic)s museum", "Here are some %(topic)s museums slot_df_name"),
            ("I'd like to go to a %(topic)s museum", "These are %(topic)s museums in Stuttgart slot_df_name"),
            ("Show me some %(topic)s museum in Stuttgart?", "Here are a few %(topic)s museums slot_df_name"),
            ("I want to go to a %(topic)s museum", "Here are some %(topic)s museums slot_df_name"),
            ("Give me some %(topic)s museums", "Here is a list of %(topic)s museums slot_df_name"),
            ("Give me some %(topic)s museums R2D2", "These are a few %(topic)s museums in Stuttgart slot_df_name"),
            ("Could you suggest me some %(topic)s museums", "Sure. Here is a list of %(topic)s museums slot_df_name"),
            ("Are there any %(topic)s museums in Stuttgart?", "The list of %(topic)s museums includes: slot_df_name"),
            ("List me some %(topic)s museums in Stuttgart", "The list of %(topic)s museums includes: slot_df_name"),
            ("List me some %(topic)s museums", "The list of %(topic)s museums includes: slot_df_name"),
            ("Could you show me some %(topic)s museums around Stuttgart", "These are %(topic)s museums around Stuttgart: slot_df_name"),
            ("What do you know about %(topic)s museums in Stuttgart", "Here are examples of %(topic)s museums around Stuttgart: slot_df_name"),
            ("Has Stuttgart %(topic)s museums?", "The list of %(topic)s museums around Stuttgart contains: slot_df_name"),
            ("Are there any %(topic)s museums located in Stuttgart?", "The list of %(topic)s museums around Stuttgart contains: slot_df_name"),
            ("Do you know any %(topic)s museums located in Stuttgart?", "We have these %(topic)s museums around Stuttgart, among others: slot_df_name"),
            ("Are you aware of any %(topic)s museums in Stuttgart?", "According to my database the list of %(topic)s museums includes: slot_df_name"),
        ]
    })

    query_domain = parametrize({
        "belief": "domain = museum",
        "user_system": [
            ("I want to visit a museum.", "What topic should the museum be about? slot_df_about"),
            ("What topics do the museums in Stuttgart have?", "Stuttgart contains museums about these topics: slot_df_about"),
            ("I want to know what types of museums you could show me in Stuttgart?", "Sure. Stuttgart has these types of museums: slot_df_about"),
            ("What museums are located in Stuttgart?", "The list of themes museums in Stuttgart have includes: slot_df_about"),
            ("What types of museums are available in Stuttgart?", "I know of these kinds of museums in Stuttgart: slot_df_about"),
            ("I'd like to go to a museum", "What type of museums would you want to visit? slot_df_about"),
            ("I would like to know more about museums", "This is a list about the topics of museums in Stuttgart: slot_df_about"),
            ("What do you know about museums?", "These are themes of museums in Stuttgart: slot_df_about"),
            ("Show we what you know about museums around Stuttgart?", "The museums in Stuttgart are about: slot_df_about")
        ]
    })
    
    query_rating = parametrize({
        "n_repetitions": 2,
        "samplers": {"number": list(range(5))},
        "belief": "domain = museum; sortby = rating; head = %(number)s",
        "user_system": [
            ("Show me the top %(number)s museums in Stuttgart.", "The top rated museums are: slot_df_name"),
            ("Can you give me a list of the %(number)s highest rated museums.", "Among the %(number)s highest rated museums in Stuttgart are: slot_df_name"),
            ("I want to go to one of the %(number)s best museums in Stuttgart.", "The %(number)s best rated museums are: slot_df_name"),
            ("Give me the %(number)s highest rated museums.", "The %(number)s museums rated highest by people are: slot_df_name"),
            ("Show me %(number)s good museums around Stuttgart.", "This is a list of museums valued highly by people: slot_df_name")
        ]
    })
    
    
    query_wheel_chair_accessible = parametrize({
        "belief": "domain = museum; wheelchair_accessible_entrance = True",
        "user_system": [
            ("Do you know museums accessible by wheechair users?", "Here is a list of museums with a wheelchair accessible entrance: slot_df_name"),
            ("I am a wheelchair user, can you show me some museums accessible for me?", "These list includes museums with an accessible entrance for wheelchairs: slot_df_name"),
            ("List some museums with accessible entrance for wheelchairs?", "I know of these museums with an accessible entrance for wheelchairs: slot_df_name"),
            ("What museums in Stuttgart have an entrance made for wheelchair users?", "These are museums people sitting in a wheelchair can enter: slot_df_name")
        ]
    })
    
    
    query_child = parametrize({
        "n_repetitions": 2,
        "samplers": {"topic": domain_sampler['museum']['about']},
        "belief": "domain = museum; for_children = 1; about = %(topic)s",
        "user_system": [
            ("My kid likes %(topic)s do you have any museums about this topic?", "Here is a list of museums about %(topic)s: slot_df_name"),
            ("Are there museums about %(topic)s suitable for children in Stuttgart?", "These are %(topic)s themed museums suitable for children: slot_df_name"),
            ("Can you show me %(topic)s museums my child would like to visit?", "Here are some %(topic)s museums that are enjoyable for children: slot_df_name"),
            ("Is there any %(topic)s museum my child would enjoy?", "slot_entity_name is a %(topic)s museum also made for children.")
        ]
    })

    

    # query_url_by_topic = parametrize({
    #     "n_repetitions": 2,
    #     "belief": "df = domains['museum'].query('about == \"%(topic)s\"') ; url = df['url'].tolist()",
    #     "samplers": {"topic": domain_sampler['museum']['about']},
    #     "user_system": [
    #         ("Can you give me urls to any museums about %(topic)s?", 
    #             "Here are urls to the websites of %(topic)s museums: {templates.list(url)}"),
    #         ("Guide me to websites about %(topic)s museums.",
    #             "These are links to %(topic)s museums: {templates.list(url)}"),
    #         ("Provide me some links to websites about %(topic)s museums.",
    #             "This is a list of urls to websites about  %(topic)s museums: {templates.list(url)}"),
    #         ("Show me links to homepages of museums about %(topic)s.",
    #             "This list contains links to websites about %(topic)s museums: {templates.list(url)}"),
    #         ("Direct me to the web pages of museums about %(topic)s.",
    #             "This list contains urls to websites about %(topic)s museums: {templates.list(url)}"),
    #         ("Could you provide me links to museums about %(topic)s.",
    #             "I know of these websites about %(topic)s museums in Stuttgart: {templates.list(url)}")
    #     ]
    # })

    return [*query_by_type, *query_domain, *query_rating, *query_wheel_chair_accessible, *query_child]
