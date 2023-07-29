def main(parametrize):
    res = []

    # asking about restaurants in general
    res.append(parametrize({
        "belief": "domain = restaurant",
        "user_system": [
            ("I want to go to a restaurant",
                "What kind of restaurants do you like? slot_df_cuisine"),
            ("I want to eat some food",
                "What type of food do you want to eat? slot_df_cuisine"),
            ("Do you know any restaurants?",
                "Sure. Which cuisines should the restaurant serve? slot_df_cuisine"),
            ("Where can i grab something to eat?",
                "What cuisines are you interested in? slot_df_cuisine"),
            ("Are there any restaurants you know of?",
                "Yes! I know restaurants that serve the following cuisines slot_df_cuisine"),
            ("I'd like to eat something",
                "What kind of food would you like to eat? slot_df_cuisine"),
            ("I'm hungry!",
                "You could go to a restaurant. What kind of food do you prefer? slot_df_cuisine"),
            ("Suggest some restaurants",
                "Sure, please let me know what kind of food you like? slot_df_cuisine"),
            ("Recommend me a restaurant in Stuttgart",
                "There are a lot of restaurants, so let's try to narrow it down. What cuisine do you prefer? slot_df_cuisine"),
            ("What can you tell me about restaurants here in Stuttgart?",
                "You can find a range of different cuisines around here. What do you prefer? slot_df_cuisine"),
        ]
    }))

    # choose a cuisine
    res.append(parametrize({
        "samplers": {"cuisine": lambda s: s['restaurant']['cuisine']},
        "belief": "domain = restaurant ; cuisine = %(cuisine)s",
        "user_system": [
            ("I want to eat %(cuisine)s food",
                "Here are some %(cuisine)s restaurants slot_df_name"),
            ("I'd like to get a %(cuisine)s meal",
                "These restaurants serve %(cuisine)s meals slot_df_name"),
            ("Where can i get some %(cuisine)s food?",
                "You can get %(cuisine)s food at these restaurants slot_df_name"),
            ("I want to eat %(cuisine)s",
                "Here are some %(cuisine)s restaurants slot_df_name"),
            ("give me %(cuisine)s restaurants",
                "Here are %(cuisine)s restaurants slot_df_name"),
            ("List %(cuisine)s restaurants",
                "Here is a list of %(cuisine)s restaurants slot_df_name"),
            ("How about some %(cuisine)s food?",
                "Sure, you can eat %(cuisine)s food at the following restaurants: slot_df_name"),
            ("I'm interested in %(cuisine)s cuisine",
                "Some %(cuisine)s restaurants in Stuttgart are slot_df_name"),
            ("I'm really craving %(cuisine)s food right now",
                "Here are some %(cuisine)s restaurants for you: slot_df_name"),
        ]
    }))

    # choose multiple cuisines
    res.append(parametrize({
        "belief": "domain = restaurant ; cuisine = %(cuisine1)s or %(cuisine2)s",
        "samplers": {
            "cuisine1": lambda s: s['restaurant']['cuisine'],
            "cuisine2": lambda s: s['restaurant']['cuisine']},
        "user_system": [
            ("Do you know any restaurants that are either %(cuisine1)s or %(cuisine2)s", 
                "Here are restaurants that fit your description slot_df_name"),
            ("I like %(cuisine1)s and %(cuisine2)s food",
                "Then you should like these restaurants slot_df_name"),
            ("I want food that is  %(cuisine1)s or %(cuisine2)s",
                "Then you should like these restaurants slot_df_name"),
            ("I can't choose between %(cuisine1)s or %(cuisine2)s food",
                "These are some restaurants that you might want to try: slot_df_name"),
            ("I prefer %(cuisine1)s food, but %(cuisine2)s is also good",
                "In that case, here are restaurants that might interest you: slot_df_name"),
            ("Maybe %(cuisine1)s or %(cuisine2)s food?",
                "Ok, here are restaurants that serve either %(cuisine1)s or %(cuisine2)s food: slot_df_name"),
        ]
    }))

    # follow-up questions without mention
    res.append(parametrize({
        "belief": "",
        "samplers": {
        },
        "user_system": [
            # address
            ("What is its address?",
             "The address of slot_entity_name is slot_entity_address."),
            ("Where is it located?",
                "slot_entity_name is located at slot_entity_address."),
            ("How do I get there?",
                "To get to slot_entity_name, you can drive or take public transport to slot_entity_address. Don't forget to check for train cancellations."),
            ("How do I find this restaurant?",
                "You can visit slot_entity_name at slot_entity_address."),
            ("Give me the directions to get there",
                "The address of slot_entity_name is slot_entity_address."),
            # rating (note: max rating is hardcoded)
            ("Does it have good ratings?",
                "The average rating of slot_entity_name based on user reviews is slot_entity_rating out of 5."),
            ("What is its rating?",
                "slot_entity_name has a rating of slot_entity_rating out of 5"),
            ("Do you know if that place has a good reputation?",
                "Based on user reviews, the average rating of slot_entity_name is slot_entity_rating out of 5. "),
            ("Can you look up the reviews?",
                "According to the reviews, the average rating of slot_entity_name is slot_entity_rating out of 5."),
            ("Tell me the rating",
                "slot_entity_name is rated slot_entity_rating out of 5."),
            ("How is it rated?",
                "slot_entity_name has an average rating of slot_entity_rating out of 5."),
            ("How good is it?",
                "Depends on what you consider good. slot_entity_name has a rating of slot_entity_rating out of 5."),
            ("Is it any good?",
                "See for yourself, slot_entity_name has an average rating of slot_entity_rating out of 5."),
            # phone number
            ("How do I contact them?",
                "You can contact slot_entity_name by phone at slot_entity_phone_number"),
            ("Can you call it for me?",
                "I can give you the phone number so you can do it: slot_entity_phone_number"),
            ("I would like to call them",
                "You can call slot_entity_name at slot_entity_phone_number"),
            ("What's their phone number?",
                "Their phone number is slot_entity_phone_number"),
            ("Do you have their phone number?",
                "Yes :) It's slot_entity_phone_number"),
            ("Can you make a reservation?",
                "No, make it yourself. You can call them at slot_entity_phone_number"),
            ("I wanna phone this restaurant",
                "Their phone number is slot_entity_phone_number, you're welcome"),
            # website
            ("Where can I read more about it?",
                "You can visit slot_entity_name's website: slot_entity_website"),
            ("Does it have a homepage?",
                "Yes, you can visit their homepage at slot_entity_website"),
            ("What's their website?",
                "Their website is slot_entity_website"),
            ("Do you have more info on it?",
                "You can find out more about slot_entity_name on their website: slot_entity_website"),
            ("What is the website address?",
                "The website of slot_entity_name is slot_entity_website"),
            # price level (note: max price level is hardcoded)
            ("What are the prices there?",
                "The price level of slot_entity_name is slot_entity_price_level out of 3."),
            ("How expensive is it?",
                "The price level of slot_entity_name is slot_entity_price_level out of 3."),
            ("Is it cheap to eat there?",
                "The price level of slot_entity_name is slot_entity_price_level out of 3."),
            ("Is it good for me if I'm on a budget?",
                "The price level of slot_entity_name is slot_entity_price_level out of 3."),
            ("How much does the food there cost?",
                "The price level of slot_entity_name is slot_entity_price_level out of 3."),
            # wheelchair access
            ("Is it accessible to wheelchair users?",
                "The wheelchair access of slot_entity_name is slot_entity_wheelchair_access."),
            ("How accessible is this place?",
                "The wheelchair access of slot_entity_name is slot_entity_wheelchair_access."),
            ("Can I go there if I'm in a wheelchair?",
                "The wheelchair access of slot_entity_name is slot_entity_wheelchair_access."),
            ("I want to know about the wheelchair accessibility there",
                "The wheelchair access of slot_entity_name is slot_entity_wheelchair_access."),
            # cuisine
            ("What kind of food do they serve?",
                "slot_entity_name serves slot_entity_cuisine food."),
            ("Which cuisine can I try there?",
                "You can try some slot_entity_cuisine cuisine at slot_entity_name."),
            ("What can I eat there?",
                "You can eat slot_entity_cuisine food at slot_entity_name."),
            ("What type of food does it have?",
                "slot_entity_name offers slot_entity_cuisine food"),
        ]
    }))

    # questions based on the name
    res.append(parametrize({
        "belief": "entity_name = %(name)s",
        "samplers": {
            "name": lambda s: s["restaurant"]["name"]},
        "user_system": [
            # address
            ("What is the address of %(name)s?",
                "The address of slot_entity_name is slot_entity_address."),
            ("Where is %(name)s located?",
                "slot_entity_name is located at slot_entity_address."),
            ("How do I get to %(name)s?",
                "To get to slot_entity_name, you can drive or take public transport to slot_entity_address."),
            ("How do I find %(name)s?",
                "You can visit slot_entity_name at slot_entity_address."),
            ("Give me directions to %(name)s?",
                "The address of slot_entity_name is slot_entity_address. Don't forget to check for train cancellations."),
            # rating (note: max rating is hardcoded)
            ("Does %(name)s have a good rating?",
                "The average rating of slot_entity_name based on user reviews is slot_entity_rating out of 5."),
            ("What is the rating of %(name)s?",
                "slot_entity_name has a rating of slot_entity_rating out of 5"),
            ("Do you know if %(name)s has a good reputation?",
                "Perhaps. I can tell you that based on user reviews of slot_entity_name, its average rating is slot_entity_rating out of 5."),
            ("Look up the reviews for %(name)s",
                "According to the reviews, the average rating of slot_entity_name is slot_entity_rating out of 5."),
            ("Tell me the rating of %(name)s",
                "slot_entity_name is rated slot_entity_rating out of 5."),
            ("How is %(name)s rated?",
                "slot_entity_name has an average rating of slot_entity_rating out of 5."),
            ("How good is %(name)s?",
                "While I can't provide any personal experiences, I know that slot_entity_name has a rating of slot_entity_rating out of 5."),
            ("Is %(name)s any good?",
                "That's for you to decide! All I can say is that slot_entity_name has an average rating of slot_entity_rating out of 5."),
            # phone number
            ("How do I contact %(name)s?",
                "You can contact slot_entity_name by phone at slot_entity_phone_number"),
            ("Can you call %(name)s for me?",
                "Please call yourself, I will give you the phone number: slot_entity_phone_number"),
            ("I need to call %(name)s",
                "You can call slot_entity_name at slot_entity_phone_number"),
            ("What's the phone number of %(name)s?",
                "Let me look it up for you... Ok, their phone number is slot_entity_phone_number"),
            ("Do you have the phone number of %(name)s?",
                "Yes, here is it: slot_entity_phone_number"),
            ("Can you make a reservation at %(name)s for me?",
                "No, but you can. Try calling them at slot_entity_phone_number"),
            ("I wanna phone %(name)s",
                "Sure, here's the phone number: slot_entity_phone_number"),
            # website
            ("Where can i read more about %(name)s?",
                "You can visit slot_entity_name's website: slot_entity_website"),
            ("Does %(name)s have a homepage?",
                "Yes, you can visit their homepage at slot_entity_website"),
            ("What's the website of %(name)s?",
                "Their website is slot_entity_website"),
            ("Do you have more info on %(name)s?",
                "You can find out more about slot_entity_name on their website: slot_entity_website"),
            ("What is the website address of %(name)s?",
                "The website of slot_entity_name is slot_entity_website"),
            # price level (note: max price level is hardcoded)
            ("What are the prices like at %(name)s?",
                "The price level of slot_entity_name is slot_entity_price_level out of 3."),
            ("How expensive is %(name)s?",
                "The price level of slot_entity_name is slot_entity_price_level out of 3."),
            ("Is it cheap to eat at %(name)s?",
                "The price level of slot_entity_name is slot_entity_price_level out of 3."),
            ("I'm on a budget, will %(name)s suit me?",
                "The price level of slot_entity_name is slot_entity_price_level out of 3."),
            ("How much does it cost to eat at %(name)s?",
                "The price level of slot_entity_name is slot_entity_price_level out of 3."),
            # wheelchair access
            ("Is %(name)s accessible to wheelchair users?",
                "The wheelchair access of slot_entity_name is slot_entity_wheelchair_access."),
            ("How accessible is %(name)s?",
                "The wheelchair access of slot_entity_name is slot_entity_wheelchair_access."),
            ("Can I get to %(name)s in a wheelchair?",
                "The wheelchair access of slot_entity_name is slot_entity_wheelchair_access."),
            ("Tell me about the wheelchair accessibility of %(name)s",
                "The wheelchair access of slot_entity_name is slot_entity_wheelchair_access."),
            # cuisine
            ("What kind of food do they serve at %(name)s?",
                "slot_entity_name serves slot_entity_cuisine food."),
            ("Which cuisine can I eat at %(name)s",
                "You can try some slot_entity_cuisine cuisine at slot_entity_name."),
            ("What can I eat if I go to %(name)s?",
                "You can eat slot_entity_cuisine food at slot_entity_name."),
            ("What type of food does %(name) specialize in?",
                "slot_entity_name specializes in slot_entity_cuisine food!"),
        ]
    }))

    # index-based
    res.append(parametrize({
        'samplers': {
            'index_text, index_int': lambda s: s['index']
        },
        'belief': "entity_index = %(index_int)s",
        "user_system": [
            # address
            ("What is the address of the %(index_text)s one?",
                "The address of slot_entity_name is slot_entity_address."),
            ("Where is number %(index_int)s located?",
                "slot_entity_name is located at slot_entity_address."),
            ("How do I get to the %(index_text)s one on the list?",
                "To get to slot_entity_name, you can drive or take public transport to slot_entity_address."),
            ("How do I find that %(index_text)s one?",
                "You can visit slot_entity_name at slot_entity_address."),
            ("Give me directions to the %(index_int) one",
                "The address of slot_entity_name is slot_entity_address."),
            # rating (note: max rating is hardcoded)
            ("Does the %(index_text)s one have a good rating?",
                "The average rating of slot_entity_name based on user reviews is slot_entity_rating out of 5."),
            ("What is the rating of number %(index_int)s?",
                "slot_entity_name has a rating of slot_entity_rating out of 5"),
            ("Does the %(index_text)s one have a good reputation?",
                "Based on user reviews of slot_entity_name, its average rating is slot_entity_rating out of 5."),
            ("Look up the reviews for number %(index_int)s",
                "According to the reviews, the average rating of slot_entity_name is slot_entity_rating out of 5."),
            ("Tell me the rating of the %(index_text)s one",
                "slot_entity_name is rated slot_entity_rating out of 5."),
            ("How is number %(index_int)s rated?",
                "slot_entity_name has an average rating of slot_entity_rating out of 5."),
            ("How good is that %(index_text)s one from the list?",
                "slot_entity_name has a rating of slot_entity_rating out of 5."),
            ("Is the %(index_text)s one any good?",
                "It has an average rating of slot_entity_rating out of 5."),
            # phone number
            ("How do I contact the %(index_text)s one?",
                "You can contact slot_entity_name by phone at slot_entity_phone_number"),
            ("I want to call the %(index_text)s one on your list",
                "No problem, you can call slot_entity_name at slot_entity_phone_number"),
            ("What's the phone number of the %(index_text)s one?",
                "Their phone number is slot_entity_phone_number"),
            ("Do you have the phone number of nr %(index_int)s?",
                "Yes, the phone number is slot_entity_phone_number"),
            # website
            ("Give me the website of the %(index_text)s one",
                "The website address is slot_entity_website"),
            ("Does the %(index_text)s one have a homepage?",
                "Yes, their homepage is slot_entity_website"),
            ("What's the website of nr %(index_int)s?",
                "Their website is slot_entity_website"),
            # price level (note: max price level is hardcoded)
            ("How expensive is the %(index_text)s one?",
                "The price level of slot_entity_name is slot_entity_price_level out of 3."),
            ("What is the price level of the %(index_text)s ine?",
                "The price level of slot_entity_name is slot_entity_price_level out of 3."),
            # wheelchair access
            ("Is the %(index_text)s one accessible to wheelchair users?",
                "The wheelchair access of slot_entity_name is slot_entity_wheelchair_access."),
            ("How accessible is number %(index_int)s on the list?",
                "The wheelchair access of slot_entity_name is slot_entity_wheelchair_access."),
            ("Can I go to the %(index_text)s one in a wheelchair?",
                "The wheelchair access of slot_entity_name is slot_entity_wheelchair_access."),
            ("Tell me about the wheelchair accessibility of that %(index_text)s place",
                "The wheelchair access of slot_entity_name is slot_entity_wheelchair_access."),
        ]
    }))

    # best rating TODO number of top entries is inconsistent
    res.append(parametrize({
        "belief": "domain = restaurants ; head = 5 ; sortby = rating",
        "samplers": {},
        "user_system": [
            ("What are the best five restaurants?",
                "Here are the five highest-rated restaurants: slot_df_name"),
            ("What are the top 5 restaurants??",
                "Here are the five highest-rated restaurants: slot_df_name"),
            ("Give me the top-5 of restaurants!",
                "The five highest-rated restaurants are: slot_df_name"),
            ("Which restaurants have the highest rating?",
                "Here are the five highest-rated restaurants: slot_df_name"),
            ("Do you know which restaurants are highest rated?",
                "Here are the five highest-rated restaurants: slot_df_name"),
            ("I'm interested which restaurants are best rated",
                "Here are the five highest-rated restaurants: slot_df_name"),
        ]
    }))

    # best rating filtered by cuisine
    res.append(parametrize({
        "belief": "domain = restaurants ; head = 3 ; sortby = rating; cuisine = %(cuisine)s",
        "samplers": {"cuisine": lambda s: s['restaurant']['cuisine']},
        "user_system": [
            ("What are the best %(cuisine)s restaurants in town?",
                "The three highest-rated %(cuisine)s restaurants are: slot_df_name"),
            ("What are the top 3 restaurants that serve %(cuisine)s food",
                "Here are the three highest-rated %(cuisine)s restaurants: slot_df_name"),
            ("Give me the top-3 %(cuisine)s restaurants!",
                "The three highest-rated %(cuisine)s restaurants are: slot_df_name"),
            ("Which %(cuisine)s restaurants have the highest rating?",
                "Here are the three highest rated restaurants: slot_df_name"),
            ("Do you know which %(cuisine)s restaurants are highest rated?",
             "Here are the three highest-rated %(cuisine)s restaurants: slot_df_name"),
            ("What is the best restaurant that serves %(cuisine)s cuisine?",
                "Here are the three highest-rated %(cuisine)s restaurants: slot_df_name"),
        ]
    }))

    # TODO most expensive ones
    res.append(parametrize({
        "belief": "domain = restaurants ; price_level = 3",
        "samplers": {},
        "user_system": [
            ('What are the most expensive restaurants?', 'Here is a list of the most expensive restaurants: slot_df_name'),
            ('I want to eat in a really expensive restaurant. Can you show me some?', 'Sure. These restaurants fall in the category expensive: slot_df_name'),
            ('Give me a list of the most expensive restaurants!', 'The list of expensive restaurants includes: slot_df_name'),
            ('Suggest me some of the most expensive restaurants?', 'These belong to the most expensive restaurants: slot_df_name'), 
            ('Can you show me the most expensive restaurants?', 'Yes, these are the most expensive ones: slot_df_name')
        ]
    }))

    # TODO cheapest ones
    res.append(parametrize({
        "belief": "domain = restaurants ; price_level = 1",
        "samplers": {},
        "user_system": [
            ('What are the cheapest restaurants?', 
                'Here is a list of the cheapest restaurants: slot_df_name'),
            ('I need to save money. Can you suggest me some restaurants?', 
                'If you want to save money you could be interested in these cheap restaurants: slot_df_name'),
            ('List me the cheapest restaurants you know?', 
                'Among the cheapest restaurants we have: slot_df_name'),
            ('Do you have any suggestions for a cheap restaurants?', 
                'I could suggest you these cheap restaurants: slot_df_name'),
            ('Show me a list of the cheapest restaurants!', 
                'Here is a list of some of the cheapest restaurants: slot_df_name')]
        ]
    }))
    
    
    # TODO only with wheelchair access
    res.append(parametrize({
        "belief": "domain = restaurants ; wheelchair_access = TRUE",
        "samplers": {},
        "user_system": [
            ('Show me restaurants with an entrance accessible by wheelchair?', 
                'This is a list contains restaurants with an entrance accessible by wheelchair: slot_df_name'),
            ('Can you show me restaurants I can enter with a wheelchair?', 
                'These are restaurants you could enter with a wheelchair: slot_df_name'),
            ('Do you know restaurants whose entrance is accesible by wheelchair?', 
                'Here are some restaurants with an entrance suitable for wheelchairs: slot_df_name'),
            ('Are there restaurants with an entrance a wheelchair can pass?', 
                'Sure. The entrance of these restaurants are accessible for wheelchairs: slot_df_name'),
            ('I am sitting in a wheelchair. Can you suggest me some restaurants I can enter?', 
                'These are restaurants you can enter with your wheelchair: slot_df_name'),
            ('List me some restaurants I can enter with my wheelchair!', 
                'If you are sitting in a wheelchair, you could pass the entrance of the these restaurants: slot_df_name')
        ]
    }))

    return res
