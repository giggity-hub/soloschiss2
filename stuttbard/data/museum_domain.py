def main(domain_sampler, parametrize):

    query_by_type = parametrize({
        "n_repetitions": 2,
        "samplers": {"topic": domain_sampler['museum']['about']},
        "belief": "df = domains['museum'].query('about == \"%(topic)s\"') ; names = df['name'].tolist()",
        "user_system": [
            ("I want to visit a %(topic)s museum", "Here are some %(topic)s museums {templates.list(names)}"),
            ("I'd like to go to a %(topic)s museum", "These are %(topic)s museums in Stuttgart {templates.list(names)}"),
            ("Show me some %(topic)s museum in Stuttgart?", "Here are a few %(topic)s museums {templates.list(names)}"),
            ("I want to go to a %(topic)s museum", "Here are some %(topic)s museums {templates.list(names)}"),
            ("Give me some %(topic)s museums", "Here is a list of %(topic)s museums {templates.list(names)}"),
            ("Give me some %(topic)s museums R2D2", "These are a few %(topic)s museums in Stuttgart {templates.list(names)}"),
            ("Could you suggest me some %(topic)s museums", "Sure. Here is a list of %(topic)s museums {templates.list(names)}"),
            ("Are there any %(topic)s museums in Stuttgart?", "The list of %(topic)s museums includes: {templates.list(names)}"),
            ("List me some %(topic)s museums in Stuttgart", "The list of %(topic)s museums includes: {templates.list(names)}"),
            ("List me some %(topic)s museums", "The list of %(topic)s museums includes: {templates.list(names)}"),
            ("Could you show me some %(topic)s museums around Stuttgart", "These are %(topic)s museums around Stuttgart: {templates.list(names)}"),
            ("What do you know about %(topic)s museums in Stuttgart", "Here are examples of %(topic)s museums around Stuttgart: {templates.list(names)}"),
            ("Has Stuttgart %(topic)s museums?", "The list of %(topic)s museums around Stuttgart contains: {templates.list(names)}"),
            ("Are there any %(topic)s museums located in Stuttgart?", "The list of %(topic)s museums around Stuttgart contains: {templates.list(names)}"),
            ("Do you know any %(topic)s museums located in Stuttgart?", "We have these %(topic)s museums around Stuttgart, among others: {templates.list(names)}"),
            ("Are you aware of any %(topic)s museums in Stuttgart?", "According to my database the list of %(topic)s museums includes: {templates.list(names)}"),
        ]
    })

    query_domain = parametrize({
        "belief": "df = domains['museum'] ; topic = df['about'].unique()",
        "user_system": [
            ("I want to visit a museum.", "What topic should the museum be about? {templates.list(topic)}"),
            ("What topics do the museums in Stuttgart have?", "Stuttgart contains museums about these topics: {templates.list(cuisines)}"),
            ("I want to know what types of museums you could show me in Stuttgart?", "Sure. Stuttgart has these types of museums: {templates.list(cuisines)}"),
            ("What museums are located in Stuttgart?", "The list of themes museums in Stuttgart have includes: {templates.list(cuisines)}"),
            ("What types of museums are available in Stuttgart?", "I know of these kinds of museums in Stuttgart: {templates.list(cuisines)}"),
            ("I'd like to go to a museum", "What type of museums would you want to visit? {templates.list(topic)}"),
            ("I would like to know more about museums", "This is a list about the topics of museums in Stuttgart: {templates.list(topic)}"),
            ("What do you know about museums?", "These are themes of museums in Stuttgart: {templates.list(topic)}"),
            ("Show we what you know about museums around Stuttgart?", "The museums in Stuttgart are about: {templates.list(topic)}")
        ]
    })

    query_url_by_topic = parametrize({
        "n_repetitions": 2,
        "belief": "df = domains['museum'].query('about == \"%(topic)s\"') ; url = df['url'].tolist()",
        "samplers": {"topic": domain_sampler['museum']['about']},
        "user_system": [
            ("Can you give me urls to any museums about %(topic)s?", 
                "Here are urls to the websites of %(topic)s museums: {templates.list(url)}"),
            ("Guide me to websites about %(topic)s museums.",
                "These are links to %(topic)s museums: {templates.list(url)}"),
            ("Provide me some links to websites about %(topic)s museums.",
                "This is a list of urls to websites about  %(topic)s museums: {templates.list(url)}"),
            ("Show me links to homepages of museums about %(topic)s.",
                "This list contains links to websites about %(topic)s museums: {templates.list(url)}"),
            ("Direct me to the web pages of museums about %(topic)s.",
                "This list contains urls to websites about %(topic)s museums: {templates.list(url)}"),
            ("Could you provide me links to museums about %(topic)s.",
                "I know of these websites about %(topic)s museums in Stuttgart: {templates.list(url)}")
        ]
    })

    return [*query_by_type, *query_domain, *query_url_by_topic]
