def main(domain_sampler, parametrize):
    return []

    call_by_mention = parametrize({
        "belief": "action = call",
        "user_system": [
            ("Call them", "Calling {phone_number} ..."),
            ("Please call their telephone number", "Calling {phone_number} ..."),
            ("Give them a call", "Calling {phone_number} ...")
        ]
    })

    call_by_name = parametrize({
        "belief": "action = call",
        "samplers": {"name": domain_sampler['name']},
        "user_system": [
            ("Call the phone number of the %(name)s please", "Calling {phone_number} ..."),
            ("Give the %(name)s a call", "Calling {phone_number} ..."),
            ("Ring up the %(name)s", "Calling {phone_number} ...")
        ]
    })

    # call_by_index_and_domain = parametrize({
    #     "belief": "row = df.iloc[%(index_int)s] ; phone_number = row['phone_number'] ; actions.call(phone_number)",
    #     "samplers": {
    #         "index_str, index_int": domain_sampler['index'],
    #         "domain": domain_sampler["keys"]},
    #     "user_system": [
    #         ("I want to make a call to the %(index_str)s %(domain)s", "Calling {phone_number} ..."),
    #         ("Connect me with the %(index_str)s via phone", "Calling {phone_number} ..."),
    #         ("Call the %(index_str)s %(domain)s", "Calling {phone_number} ...")
    #     ]
    # })

    open_website_by_mention = parametrize({
        "belief": "action = open_website",
        "user_system": [
            ("Can you show me the website?", "Opening {url} in the browser ..."),
            ("Take me to their url", "Opening {url} in the browser ..."),
            ("Open their website", "Opening {url} in the browser ...")
        ]
    })

    return [*call_by_mention, *call_by_name, *call_by_index_and_domain, *open_website_by_mention]
