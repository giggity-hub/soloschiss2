def main(parametrize):

    res = []
    
    a = [('I want to visit a %(topic)s museum', 'Here are some %(topic)s museums slot_df_name', 'domain = museum ; about = %(topic)s'), ("I'd like to go to a %(topic)s museum", 'These are %(topic)s museums in Stuttgart slot_df_name', 'domain = museum ; about = %(topic)s'), ('Show me some %(topic)s museum in Stuttgart?', 'Here are a few %(topic)s museums slot_df_name', 'domain = museum ; about = %(topic)s'), ('I want to go to a %(topic)s museum', 'Here are some %(topic)s museums slot_df_name', 'domain = museum ; about = %(topic)s'), ('Give me some %(topic)s museums', 'Here is a list of %(topic)s museums slot_df_name', 'domain = museum ; about = %(topic)s'), ('Give me some %(topic)s museums R2D2', 'These are a few %(topic)s museums in Stuttgart slot_df_name', 'domain = museum ; about = %(topic)s'), ('Could you suggest me some %(topic)s museums', 'Sure. Here is a list of %(topic)s museums slot_df_name', 'domain = museum ; about = %(topic)s'), ('Are there any %(topic)s museums in Stuttgart?', 'The list of %(topic)s museums includes: slot_df_name', 'domain = museum ; about = %(topic)s'), ('List me some %(topic)s museums in Stuttgart', 'The list of %(topic)s museums includes: slot_df_name', 'domain = museum ; about = %(topic)s'), ('List me some %(topic)s museums', 'The list of %(topic)s museums includes: slot_df_name', 'domain = museum ; about = %(topic)s'), ('Could you show me some %(topic)s museums around Stuttgart', 'These are %(topic)s museums around Stuttgart: slot_df_name', 'domain = museum ; about = %(topic)s'), ('What do you know about %(topic)s museums in Stuttgart', 'Here are examples of %(topic)s museums around Stuttgart: slot_df_name', 'domain = museum ; about = %(topic)s'), ('Has Stuttgart %(topic)s museums?', 'The list of %(topic)s museums around Stuttgart contains: slot_df_name', 'domain = museum ; about = %(topic)s'), ('Are there any %(topic)s museums located in Stuttgart?', 'The list of %(topic)s museums around Stuttgart contains: slot_df_name', 'domain = museum ; about = %(topic)s'), ('Do you know any %(topic)s museums located in Stuttgart?', 'We have these %(topic)s museums around Stuttgart, among others: slot_df_name', 'domain = museum ; about = %(topic)s'), ('Are you aware of any %(topic)s museums in Stuttgart?', 'According to my database the list of %(topic)s museums includes: slot_df_name', 'domain = museum ; about = %(topic)s')]

    b = [('I want to visit a museum.', 'What topic should the museum be about? slot_df_about', 'domain = museum'), ('What topics do the museums in Stuttgart have?', 'Stuttgart contains museums about these topics: slot_df_about', 'domain = museum'), ('I want to know what types of museums you could show me in Stuttgart?', 'Sure. Stuttgart has these types of museums: slot_df_about', 'domain = museum'), ('What museums are located in Stuttgart?', 'The list of themes museums in Stuttgart have includes: slot_df_about', 'domain = museum'), ('What types of museums are available in Stuttgart?', 'I know of these kinds of museums in Stuttgart: slot_df_about', 'domain = museum'), ("I'd like to go to a museum", 'What type of museums would you want to visit? slot_df_about', 'domain = museum'), ('I would like to know more about museums', 'This is a list about the topics of museums in Stuttgart: slot_df_about', 'domain = museum'), ('What do you know about museums?', 'These are themes of museums in Stuttgart: slot_df_about', 'domain = museum'), ('Show we what you know about museums around Stuttgart?', 'The museums in Stuttgart are about: slot_df_about', 'domain = museum')]
    
    c = [('Show me the top %(number)s museums in Stuttgart.', 'The top rated museums are: slot_df_name', 'domain = museum; sortby = rating; head = %(number)s'), ('Can you give me a list of the %(number)s highest rated museums.', 'Among the %(number)s highest rated museums in Stuttgart are: slot_df_name', 'domain = museum; sortby = rating; head = %(number)s'), ('I want to go to one of the %(number)s best museums in Stuttgart.', 'The %(number)s best rated museums are: slot_df_name', 'domain = museum; sortby = rating; head = %(number)s'), ('Give me the %(number)s highest rated museums.', 'The %(number)s museums rated highest by people are: slot_df_name', 'domain = museum; sortby = rating; head = %(number)s'), ('Show me %(number)s good museums around Stuttgart.', 'This is a list of museums valued highly by people: slot_df_name', 'domain = museum; sortby = rating; head = %(number)s')]

    d = [('Do you know museums accessible by wheechair users?', 'Here is a list of museums with a wheelchair accessible entrance: slot_df_name', 'domain = museum; wheelchair_accessible_entrance = True'), ('I am a wheelchair user, can you show me some museums accessible for me?', 'These list includes museums with an accessible entrance for wheelchairs: slot_df_name', 'domain = museum; wheelchair_accessible_entrance = True'), ('List some museums with accessible entrance for wheelchairs?', 'I know of these museums with an accessible entrance for wheelchairs: slot_df_name', 'domain = museum; wheelchair_accessible_entrance = True'), ('What museums in Stuttgart have an entrance made for wheelchair users?', 'These are museums people sitting in a wheelchair can enter: slot_df_name', 'domain = museum; wheelchair_accessible_entrance = True')]
    
    e = [('My kid likes %(topic)s do you have any museums about this topic?', 'Here is a list of museums about %(topic)s: slot_df_name', 'domain = museum; for_children = 1; about = %(topic)s'), ('Are there museums about %(topic)s suitable for children in Stuttgart?', 'These are %(topic)s themed museums suitable for children: slot_df_name', 'domain = museum; for_children = 1; about = %(topic)s'), ('Can you show me %(topic)s museums my child would like to visit?', 'Here are some %(topic)s museums that are enjoyable for children: slot_df_name', 'domain = museum; for_children = 1; about = %(topic)s'), ('Is there any %(topic)s museum my child would enjoy?', 'slot_entity_name is a %(topic)s museum also made for children.', 'domain = museum; for_children = 1; about = %(topic)s')]
    
    
    # single column queries (i.e. single attribute queries) based on entity_name belief state
    f = [('What house number has the %(name)s museum in Stuttgart?', 'The house number of the slot_entity_name is slot_entity_house_number.', 'domain = museum; entity_name = %(name)s'), ('Do you know the house number of the %(name)s museum?', 'Sure, it is slot_entity_house_number.', 'domain = museum; entity_name = %(name)s'), ('Can you tell me the adress number of the %(name)s museum?', 'The museum has the adress number: slot_entity_house_number.', 'domain = museum; entity_name = %(name)s'), ('What building number has the %(name)s museum in Stuttgart?', 'The building number is: slot_entity_house_number.', 'domain = museum; entity_name = %(name)s'), ('Give me the house number of the %(name)s museum.', 'slot_entity_name has the house number slot_entity_house_number.', 'domain = museum; entity_name = %(name)s'), ('Tell me the street of the %(name)s museum in Stuttgart.', 'The slot_entity_name museum resides in the slot_entity_street', 'domain = museum; entity_name = %(name)s'), ('What was the street of the %(name)s museum?', 'For slot_entity_name the street name is slot_entity_street', 'domain = museum; entity_name = %(name)s'), ('Can you provide me the street name of the %(name)s museum?', 'According, to my database the street is slot_entity_street', 'domain = museum; entity_name = %(name)s'), ('Can you give me the google plus code for the %(name)s museum?', 'The google plus code for slot_entity_name is slot_entity_plus_code.', 'domain = museum; entity_name = %(name)s'), ('I want to look up the %(name)s museum in google maps?', 'I can provide you with the google plus code: slot_entity_plus_code, for the slot_entity_name museum.', 'domain = museum; entity_name = %(name)s'), ('In which area of Stuttgart is the %(name)s museum?', 'The museum is placed in slot_entity_area.', 'domain = museum; entity_name = %(name)s'), ('Where is the %(name)s museum in Stuttgart?', 'According to my knowledge the slot_entity_name is in slot_entity_area.', 'domain = museum; entity_name = %(name)s'), ('Show me the area of the %(name)s museum', 'The slot_entity_name museum resides in the area of slot_entity_area.', 'domain = museum; entity_name = %(name)s'), ('Show the official phone number of the %(name)s museum!', 'The phone number of the slot_entity_name is slot_entity_phone_number.', 'domain = museum; entity_name = %(name)s'), ('I want to call the %(name)s museum. Give me the number!', 'The slot_entity_name museum can be reached by the phone number slot_entity_phone_number.', 'domain = museum; entity_name = %(name)s'), ('What is the phone number of the %(name)s museum?', 'The phone number is slot_entity_phone_number.', 'domain = museum; entity_name = %(name)s'), ('Show me the google maps rating of the %(name)s museum in Stuttgart.', 'According to the reviews the slot_entity_name museum achieved an average rating of slot_entity_rating.', 'domain = museum; entity_name = %(name)s'), ('What rating does the %(name)s museum in Stuttgart have on google maps.', 'The slot_entity_name museum has an average rating of slot_entity_rating.', 'domain = museum; entity_name = %(name)s'), ('How popular is the %(name)s museum in Stuttgart?.', 'The reviews give the slot_entity_name museum an average rating of slot_entity_rating.', 'domain = museum; entity_name = %(name)s'), ('Is the %(name)s museum in Stuttgart good?', 'In reviews the museum achieved an average rating of slot_entity_rating.', 'domain = museum; entity_name = %(name)s'), ('Do people like the %(name)s museum?', 'To my knowledge the museum achieved slot_entity_rating as average rating from reviews.', 'domain = museum; entity_name = %(name)s'), ('Can you recommend the %(name)s museum in Stuttgart?', 'Well, the %(name)s museum has an average rating of slot_entity_rating on google maps.', 'domain = museum; entity_name = %(name)s'), ('Is the %(name)s museum in Stuttgart worth a visit?', 'slot_entity_rating is the average rating of the place on gooogle maps.', 'domain = museum; entity_name = %(name)s'), ('What is the %(name)s museum about?', 'The slot_entity_name museum covers slot_entity_about or more precisely slot_entity_about_specific.', 'domain = museum; entity_name = %(name)s'), ('Do you know the theme of the %(name)s museum in Stuttgart?', 'The theme of slot_entity_name museum is slot_entity_about_specific, i.e. it is about slot_entity_about.', 'domain = museum; entity_name = %(name)s'), ('What topic has the %(name)s museum in Stuttgart?', 'The slot_entity_name museum has an exhibition on slot_entity_about_specific. Thus it is a slot_entity_about_specific museum.', 'domain = museum; entity_name = %(name)s'), ('Show me the topic of the %(name)s museum.', 'The slot_entity_name museum covers slot_entity_about_specific and therefore is an slot_entity_about_specific museum.', 'domain = museum; entity_name = %(name)s'), ('I am interested in the %(name)s museum, can you provide me a link to the website?', 'Sure, the website link is slot_entity_website for the slot_entity_name museum.', 'domain = museum; entity_name = %(name)s'), ('Do you have any related links to the %(name)s museum?', 'The official link to the slot_entity_name museum is: slot_entity_website.', 'domain = museum; entity_name = %(name)s'), ('Can you give me additional information on the %(name)s museum?', 'You can find more information about the slot_entity_name museum on slot_entity_website.', 'domain = museum; entity_name = %(name)s'), ('Show me the website of the %(name)s museum.', 'The link to the official website is slot_entity_website.', 'domain = museum; entity_name = %(name)s'), ('Direct me to the website of the %(name)s museum!', 'The website of the slot_entity_name museum can be reached under slot_entity_website.', 'domain = museum; entity_name = %(name)s')]
    
    
    # single column queries (i.e. single attribute queries) based on entity_index belief state
    g = [('Does the %(index_text)s museum has an accessible entrance for wheelchairs?', 'The entrance of the slot_entity_name museum is for wheelchairs: slot_entity_wheelchair_accessible_entrance.', 'domain = museum; entity_index = %(index_int)s'), ('What is the adress of the %(index_text)s museum?', 'The adress of the slot_entity_name museum is slot_entity_vicinity.', 'domain = museum; entity_index = %(index_int)s'), ('Can you give me the link to the website of the %(index_text)s museum?', 'The link to the %(index_text)s museum is slot_entity_website.', 'domain = museum; entity_index = %(index_int)s'), ('Give me the house number of the %(index_text)s museum!', 'The slot_entity_name museum has the house number slot_entity_house_number.', 'domain = museum; entity_index = %(index_int)s'), ('Im interested in the %(index_text)s museum. Show me the phone number!', 'slot_entity_phone_number is the phone number of the slot_entity_name museum.', 'domain = museum; entity_index = %(index_int)s'), ('Give me the phone number of the %(index_text)s one!', 'The slot_entity_name museum can be reached under slot_entity_phone_number.', 'domain = museum; entity_index = %(index_int)s'), ('In which street is the %(index_text)s one', 'The slot_entity_name museum sits in the slot_entity_street street.', 'domain = museum; entity_index = %(index_int)s'), ('I want to know the rating of the %(index_text)s one', 'The %(index_text)s museum has an average rating of slot_entity_rating on google maps.', 'domain = museum; entity_index = %(index_int)s'), ('How popular is the %(index_text)s museum?', 'The average rating of the %(index_text)s museum is slot_entity_rating.', 'domain = museum; entity_index = %(index_int)s'), ('Could you give me the google plus code of the %(index_text)s one?', 'Sure, the google plus code of the slot_entity_name museum is slot_entity_plus_code.', 'domain = museum; entity_index = %(index_int)s'), ('What is the topic of the %(index_text)s museum?', 'The %(index_text)s museum is about slot_entity_about or more specific about slot_entity_about_specific.', 'domain = museum; entity_index = %(index_int)s'), ('I would like to visit the %(index_text)s museum. In which area is it?', 'The slot_entity_name museum is in the slot_entity_area.', 'domain = museum; entity_index = %(index_int)s')]
        

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


    return res