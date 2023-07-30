def unroll_belief_state(moped):
    res = []
    for user, system in moped['user_system']:
        res.append((user, system, moped['belief']))

    return res

moped = {
        'samplers': {'index_text, index_int': lambda s : s['index']},
        'belief': "domain = museum; entity_index = %(index_int)s",
        "user_system": [
            ("Does the %(index_text)s museum has an accessible entrance for wheelchairs?", "The entrance of the slot_entity_name museum is for wheelchairs: slot_entity_wheelchair_accessible_entrance."),
            ("What is the adress of the %(index_text)s museum?", "The adress of the slot_entity_name museum is slot_entity_vicinity."),
            ("Can you give me the link to the website of the %(index_text)s museum?", "The link to the %(index_text)s museum is slot_entity_website."),
            ("Give me the house number of the %(index_text)s museum!", "The slot_entity_name museum has the house number slot_entity_house_number."),
            ("Im interested in the %(index_text)s museum. Show me the phone number!", "slot_entity_phone_number is the phone number of the slot_entity_name museum."),
            ("Give me the phone number of the %(index_text)s one!", "The slot_entity_name museum can be reached under slot_entity_phone_number."),
            ("In which street is the %(index_text)s one", "The slot_entity_name museum sits in the slot_entity_street street."),
            ("I want to know the rating of the %(index_text)s one", "The %(index_text)s museum has an average rating of slot_entity_rating on google maps."),            
            ("How popular is the %(index_text)s museum?", "The average rating of the %(index_text)s museum is slot_entity_rating."),
            ("Could you give me the google plus code of the %(index_text)s one?", "Sure, the google plus code of the slot_entity_name museum is slot_entity_plus_code."),
            ("What is the topic of the %(index_text)s museum?", "The %(index_text)s museum is about slot_entity_about or more specific about slot_entity_about_specific."),
            ("I would like to visit the %(index_text)s museum. In which area is it?", "The slot_entity_name museum is in the slot_entity_area.")
        ]
    }

x = unroll_belief_state(moped)
print(x)