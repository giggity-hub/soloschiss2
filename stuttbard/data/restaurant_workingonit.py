def main(parametrize):
    
    # asking about restaurants in general
    a = [('I want to go to a restaurant', 'What kind of restaurants do you like? slot_df_cuisine', 'domain = restaurant'), 
    ('I want to eat some food', 'What type of food do you want to eat? slot_df_cuisine', 'domain = restaurant'), 
    ('Do you know any restaurants?', 'Sure. Which cuisines should the restaurant serve? slot_df_cuisine', 'domain = restaurant'), 
    ('Where can i grab something to eat?', 'What cuisines are you interested in? slot_df_cuisine', 'domain = restaurant'), 
    ('Are there any restaurants you know of?', 'Yes! I know restaurants that serve the following cuisines slot_df_cuisine', 'domain = restaurant'), 
    ("I'd like to eat something", 'What kind of food would you like to eat? slot_df_cuisine', 'domain = restaurant'), 
    ("I'm hungry!", 'You could go to a restaurant. What kind of food do you prefer? slot_df_cuisine', 'domain = restaurant'), 
    ('Suggest some restaurants', 'Sure, please let me know what kind of food you like? slot_df_cuisine', 'domain = restaurant'), 
    ('Recommend me a restaurant in Stuttgart', "There are a lot of restaurants, so let's try to narrow it down. What cuisine do you prefer? slot_df_cuisine", 'domain = restaurant'), 
    ('What can you tell me about restaurants here in Stuttgart?', 'You can find a range of different cuisines around here. What do you prefer? slot_df_cuisine', 'domain = restaurant')
    ]

    # choose a cuisine
    b = [('I want to eat {restaurant_cuisine} food', 'Here are some {restaurant_cuisine} restaurants slot_df_name', 'domain = restaurant ; cuisine = {restaurant_cuisine}'),
    ("I'd like to get a {restaurant_cuisine} meal", 'These restaurants serve {restaurant_cuisine} meals slot_df_name', 'domain = restaurant ; cuisine = {restaurant_cuisine}'), 
    ('Where can i get some {restaurant_cuisine} food?', 'You can get {restaurant_cuisine} food at these restaurants slot_df_name', 'domain = restaurant ; cuisine = {restaurant_cuisine}'), 
    ('I want to eat {restaurant_cuisine}', 'Here are some {restaurant_cuisine} restaurants slot_df_name', 'domain = restaurant ; cuisine = {restaurant_cuisine}'), 
    ('Give me {restaurant_cuisine} restaurants', 'Here are {restaurant_cuisine} restaurants slot_df_name', 'domain = restaurant ; cuisine = {restaurant_cuisine}'), 
    ('List {restaurant_cuisine} restaurants', 'Here is a list of {restaurant_cuisine} restaurants slot_df_name', 'domain = restaurant ; cuisine = {restaurant_cuisine}'), 
    ('How about some {restaurant_cuisine} food?', 'Sure, you can eat {restaurant_cuisine} food at the following restaurants: slot_df_name', 'domain = restaurant ; cuisine = {restaurant_cuisine}'), 
    ("I'm interested in {restaurant_cuisine} cuisine", 'Some {restaurant_cuisine} restaurants in Stuttgart are slot_df_name', 'domain = restaurant ; cuisine = {restaurant_cuisine}'), 
    ("I'm really craving {restaurant_cuisine} food right now", 'Here are some {restaurant_cuisine} restaurants for you: slot_df_name', 'domain = restaurant ; cuisine = {restaurant_cuisine}')
    ]

    # choose multiple cuisines
    # Unfortunately choosing multiple things doesn't work with the new sampling yet
    # also the model was kind of thrown off by that so multiple options probably wasn't a good idea
    # c = [('Do you know any restaurants that are either {restaurant_cuisine1} or {restaurant_cuisine2}', 'Here are restaurants that fit your description slot_df_name', 'domain = restaurant ; cuisine = {restaurant_cuisine1} or {restaurant_cuisine2}'), ('I like {restaurant_cuisine1} and {restaurant_cuisine2} food', 'Then you should like these restaurants slot_df_name', 'domain = restaurant ; cuisine = {restaurant_cuisine1} or {restaurant_cuisine2}'), ('I want food that is  {restaurant_cuisine1} or {restaurant_cuisine2}', 'Then you should like these restaurants slot_df_name', 'domain = restaurant ; cuisine = {restaurant_cuisine1} or {restaurant_cuisine2}'), ("I can't choose between {restaurant_cuisine1} or {restaurant_cuisine2} food", 'These are some restaurants that you might want to try: slot_df_name', 'domain = restaurant ; cuisine = {restaurant_cuisine1} or {restaurant_cuisine2}'), ('I prefer {restaurant_cuisine1} food, but {restaurant_cuisine2} is also good', 'In that case, here are restaurants that might interest you: slot_df_name', 'domain = restaurant ; cuisine = {restaurant_cuisine1} or {restaurant_cuisine2}'), ('Maybe {restaurant_cuisine1} or {restaurant_cuisine2} food?', 'Ok, here are restaurants that serve either {restaurant_cuisine1} or {restaurant_cuisine2} food: slot_df_name', 'domain = restaurant ; cuisine = {restaurant_cuisine1} or {restaurant_cuisine2}')]

    # follow-up questions without mention
    d = [
        ('What is its address?', 'The address of slot_entity_name is slot_entity_address.', ''), 
        ('Where is it located?', 'slot_entity_name is located at slot_entity_address.', ''), 
        ('How do I get there?', "To get to slot_entity_name, you can drive or take public transport to slot_entity_address. Don't forget to check for train cancellations.", ''), 
        ('How do I find this restaurant?', 'You can visit slot_entity_name at slot_entity_address.', ''), 
        ('Give me the directions to get there', 'The address of slot_entity_name is slot_entity_address.', ''), 
        ('Does it have good ratings?', 'The average rating of slot_entity_name based on user reviews is slot_entity_rating out of 5.', ''), 
        ('What is its rating?', 'slot_entity_name has a rating of slot_entity_rating out of 5', ''), 
        ('Do you know if that place has a good reputation?', 'Based on user reviews, the average rating of slot_entity_name is slot_entity_rating out of 5. ', ''), 
        ('Can you look up the reviews?', 'According to the reviews, the average rating of slot_entity_name is slot_entity_rating out of 5.', ''), 
        ('Tell me the rating', 'slot_entity_name is rated slot_entity_rating out of 5.', ''), 
        ('How is it rated?', 'slot_entity_name has an average rating of slot_entity_rating out of 5.', ''), 
        ('How good is it?', 'Depends on what you consider good. slot_entity_name has a rating of slot_entity_rating out of 5.', ''), 
        ('Is it any good?', 'See for yourself, slot_entity_name has an average rating of slot_entity_rating out of 5.', ''), 
        ('How do I contact them?', 'You can contact slot_entity_name by phone at slot_entity_phone_number', ''), 
        ('Can you call it for me?', 'I can give you the phone number so you can do it: slot_entity_phone_number', ''), 
        ('I would like to call them', 'You can call slot_entity_name at slot_entity_phone_number', ''), 
        ("What's their phone number?", 'Their phone number is slot_entity_phone_number', ''), 
        ('Do you have their phone number?', "Yes :) It's slot_entity_phone_number", ''), 
        ('Can you make a reservation?', 'No, make it yourself. You can call them at slot_entity_phone_number', ''), 
        ('I wanna phone this restaurant', "Their phone number is slot_entity_phone_number, you're welcome", ''), 
        ('Where can I read more about it?', "You can visit slot_entity_name's website: slot_entity_website", ''), 
        ('Does it have a homepage?', 'Yes, you can visit their homepage at slot_entity_website', ''), 
        ("What's their website?", 'Their website is slot_entity_website', ''), 
        ('Do you have more info on it?', 'You can find out more about slot_entity_name on their website: slot_entity_website', ''), 
        ('What is the website address?', 'The website of slot_entity_name is slot_entity_website', ''), 
        ('What are the prices there?', 'The price level of slot_entity_name is slot_entity_price_level out of 3.', ''), 
        ('How expensive is it?', 'The price level of slot_entity_name is slot_entity_price_level out of 3.', ''), 
        ('Is it cheap to eat there?', 'The price level of slot_entity_name is slot_entity_price_level out of 3.', ''), 
        ("Is it good for me if I'm on a budget?", 'The price level of slot_entity_name is slot_entity_price_level out of 3.', ''), 
        ('How much does the food there cost?', 'The price level of slot_entity_name is slot_entity_price_level out of 3.', ''), 
        ('Is it accessible to wheelchair users?', 'The wheelchair access of slot_entity_name is slot_entity_wheelchair_access.', ''), 
        ('How accessible is this place?', 'The wheelchair access of slot_entity_name is slot_entity_wheelchair_access.', ''), 
        ("Can I go there if I'm in a wheelchair?", 'The wheelchair access of slot_entity_name is slot_entity_wheelchair_access.', ''), 
        ('I want to know about the wheelchair accessibility there', 'The wheelchair access of slot_entity_name is slot_entity_wheelchair_access.', ''), 
        ('What kind of food do they serve?', 'slot_entity_name serves slot_entity_cuisine food.', ''), 
        ('Which cuisine can I try there?', 'You can try some slot_entity_cuisine cuisine at slot_entity_name.', ''), 
        ('What can I eat there?', 'You can eat slot_entity_cuisine food at slot_entity_name.', ''), 
        ('What type of food does it have?', 'slot_entity_name offers slot_entity_cuisine food', '')
    ]

    # questions based on the name
    e = [('What is the address of {restaurant_name}?', 'The address of slot_entity_name is slot_entity_address.', 'entity_name = {restaurant_name}'), 
    ('Where is {restaurant_name} located?', 'slot_entity_name is located at slot_entity_address.', 'entity_name = {restaurant_name}'), 
    ('How do I get to {restaurant_name}?', 'To get to slot_entity_name, you can drive or take public transport to slot_entity_address.', 'entity_name = {restaurant_name}'), 
    ('How do I find {restaurant_name}?', 'You can visit slot_entity_name at slot_entity_address.', 'entity_name = {restaurant_name}'), 
    ('Give me directions to {restaurant_name}?', "The address of slot_entity_name is slot_entity_address. Don't forget to check for train cancellations.", 'entity_name = {restaurant_name}'), 
    ('Does {restaurant_name} have a good rating?', 'The average rating of slot_entity_name based on user reviews is slot_entity_rating out of 5.', 'entity_name = {restaurant_name}'), 
    ('What is the rating of {restaurant_name}?', 'slot_entity_name has a rating of slot_entity_rating out of 5', 'entity_name = {restaurant_name}'), 
    ('Do you know if {restaurant_name} has a good reputation?', 'Perhaps. I can tell you that based on user reviews of slot_entity_name, its average rating is slot_entity_rating out of 5.', 'entity_name = {restaurant_name}'), 
    ('Look up the reviews for {restaurant_name}', 'According to the reviews, the average rating of slot_entity_name is slot_entity_rating out of 5.', 'entity_name = {restaurant_name}'), 
    ('Tell me the rating of {restaurant_name}', 'slot_entity_name is rated slot_entity_rating out of 5.', 'entity_name = {restaurant_name}'), 
    ('How is {restaurant_name} rated?', 'slot_entity_name has an average rating of slot_entity_rating out of 5.', 'entity_name = {restaurant_name}'), 
    ('How good is {restaurant_name}?', "While I can't provide any personal experiences, I know that slot_entity_name has a rating of slot_entity_rating out of 5.", 'entity_name = {restaurant_name}'), 
    ('Is {restaurant_name} any good?', "That's for you to decide! All I can say is that slot_entity_name has an average rating of slot_entity_rating out of 5.", 'entity_name = {restaurant_name}'), 
    ('How do I contact {restaurant_name}?', 'You can contact slot_entity_name by phone at slot_entity_phone_number', 'entity_name = {restaurant_name}'), 
    ('Can you call {restaurant_name} for me?', 'Please call yourself, I will give you the phone number: slot_entity_phone_number', 'entity_name = {restaurant_name}'), 
    ('I need to call {restaurant_name}', 'You can call slot_entity_name at slot_entity_phone_number', 'entity_name = {restaurant_name}'), 
    ("What's the phone number of {restaurant_name}?", 'Let me look it up for you... Ok, their phone number is slot_entity_phone_number', 'entity_name = {restaurant_name}'), 
    ('Do you have the phone number of {restaurant_name}?', 'Yes, here is it: slot_entity_phone_number', 'entity_name = {restaurant_name}'), 
    ('Can you make a reservation at {restaurant_name} for me?', 'No, but you can. Try calling them at slot_entity_phone_number', 'entity_name = {restaurant_name}'), 
    ('I wanna phone {restaurant_name}', "Sure, here's the phone number: slot_entity_phone_number", 'entity_name = {restaurant_name}'), 
    ('Where can i read more about {restaurant_name}?', "You can visit slot_entity_name's website: slot_entity_website", 'entity_name = {restaurant_name}'), 
    ('Does {restaurant_name} have a homepage?', 'Yes, you can visit their homepage at slot_entity_website', 'entity_name = {restaurant_name}'), 
    ("What's the website of {restaurant_name}?", 'Their website is slot_entity_website', 'entity_name = {restaurant_name}'), 
    ('Do you have more info on {restaurant_name}?', 'You can find out more about slot_entity_name on their website: slot_entity_website', 'entity_name = {restaurant_name}'), 
    ('What is the website address of {restaurant_name}?', 'The website of slot_entity_name is slot_entity_website', 'entity_name = {restaurant_name}'), 
    ('What are the prices like at {restaurant_name}?', 'The price level of slot_entity_name is slot_entity_price_level out of 3.', 'entity_name = {restaurant_name}'), 
    ('How expensive is {restaurant_name}?', 'The price level of slot_entity_name is slot_entity_price_level out of 3.', 'entity_name = {restaurant_name}'), 
    ('Is it cheap to eat at {restaurant_name}?', 'The price level of slot_entity_name is slot_entity_price_level out of 3.', 'entity_name = {restaurant_name}'), 
    ("I'm on a budget, will {restaurant_name} suit me?", 'The price level of slot_entity_name is slot_entity_price_level out of 3.', 'entity_name = {restaurant_name}'), 
    ('How much does it cost to eat at {restaurant_name}?', 'The price level of slot_entity_name is slot_entity_price_level out of 3.', 'entity_name = {restaurant_name}'), 
    ('Is {restaurant_name} accessible to wheelchair users?', 'The wheelchair access of slot_entity_name is slot_entity_wheelchair_access.', 'entity_name = {restaurant_name}'), 
    ('How accessible is {restaurant_name}?', 'The wheelchair access of slot_entity_name is slot_entity_wheelchair_access.', 'entity_name = {restaurant_name}'), 
    ('Can I get to {restaurant_name} in a wheelchair?', 'The wheelchair access of slot_entity_name is slot_entity_wheelchair_access.', 'entity_name = {restaurant_name}'), 
    ('Tell me about the wheelchair accessibility of {restaurant_name}', 'The wheelchair access of slot_entity_name is slot_entity_wheelchair_access.', 'entity_name = {restaurant_name}'), 
    ('What kind of food do they serve at {restaurant_name}?', 'slot_entity_name serves slot_entity_cuisine food.', 'entity_name = {restaurant_name}'), 
    ('Which cuisine can I eat at {restaurant_name}', 'You can try some slot_entity_cuisine cuisine at slot_entity_name.', 'entity_name = {restaurant_name}'), 
    ('What can I eat if I go to {restaurant_name}?', 'You can eat slot_entity_cuisine food at slot_entity_name.', 'entity_name = {restaurant_name}'), 
    ('What type of food does {restaurant_name) specialize in?', 'slot_entity_name specializes in slot_entity_cuisine food!', 'entity_name = {restaurant_name}')
    ]

    # index-based
    f = [('What is the address of the {index_str} one?', 'The address of slot_entity_name is slot_entity_address.', 'entity_index = {index_int}'), 
    ('Where is number {index_int} located?', 'slot_entity_name is located at slot_entity_address.', 'entity_index = {index_int}'), 
    ('How do I get to the {index_str} one on the list?', 'To get to slot_entity_name, you can drive or take public transport to slot_entity_address.', 'entity_index = {index_int}'), 
    ('How do I find that {index_str} one?', 'You can visit slot_entity_name at slot_entity_address.', 'entity_index = {index_int}'), 
    ('Give me directions to the {index_int} one', 'The address of slot_entity_name is slot_entity_address.', 'entity_index = {index_int}'), 
    ('Does the {index_str} one have a good rating?', 'The average rating of slot_entity_name based on user reviews is slot_entity_rating out of 5.', 'entity_index = {index_int}'), 
    ('What is the rating of number {index_int}?', 'slot_entity_name has a rating of slot_entity_rating out of 5', 'entity_index = {index_int}'), 
    ('Does the {index_str} one have a good reputation?', 'Based on user reviews of slot_entity_name, its average rating is slot_entity_rating out of 5.', 'entity_index = {index_int}'), 
    ('Look up the reviews for number {index_int}', 'According to the reviews, the average rating of slot_entity_name is slot_entity_rating out of 5.', 'entity_index = {index_int}'), 
    ('Tell me the rating of the {index_str} one', 'slot_entity_name is rated slot_entity_rating out of 5.', 'entity_index = {index_int}'), 
    ('How is number {index_int} rated?', 'slot_entity_name has an average rating of slot_entity_rating out of 5.', 'entity_index = {index_int}'), 
    ('How good is that {index_str} one from the list?', 'slot_entity_name has a rating of slot_entity_rating out of 5.', 'entity_index = {index_int}'), 
    ('Is the {index_str} one any good?', 'It has an average rating of slot_entity_rating out of 5.', 'entity_index = {index_int}'), 
    ('How do I contact the {index_str} one?', 'You can contact slot_entity_name by phone at slot_entity_phone_number', 'entity_index = {index_int}'), 
    ('I want to call the {index_str} one on your list', 'No problem, you can call slot_entity_name at slot_entity_phone_number', 'entity_index = {index_int}'), 
    ("What's the phone number of the {index_str} one?", 'Their phone number is slot_entity_phone_number', 'entity_index = {index_int}'), 
    ('Do you have the phone number of nr {index_int}?', 'Yes, the phone number is slot_entity_phone_number', 'entity_index = {index_int}'), 
    ('Give me the website of the {index_str} one', 'The website address is slot_entity_website', 'entity_index = {index_int}'), 
    ('Does the {index_str} one have a homepage?', 'Yes, their homepage is slot_entity_website', 'entity_index = {index_int}'), 
    ("What's the website of nr {index_int}?", 'Their website is slot_entity_website', 'entity_index = {index_int}'), 
    ('How expensive is the {index_str} one?', 'The price level of slot_entity_name is slot_entity_price_level out of 3.', 'entity_index = {index_int}'), 
    ('What is the price level of the {index_str} one?', 'The price level of slot_entity_name is slot_entity_price_level out of 3.', 'entity_index = {index_int}'), 
    ('Is the {index_str} one accessible to wheelchair users?', 'The wheelchair access of slot_entity_name is slot_entity_wheelchair_access.', 'entity_index = {index_int}'), 
    ('How accessible is number {index_int} on the list?', 'The wheelchair access of slot_entity_name is slot_entity_wheelchair_access.', 'entity_index = {index_int}'), 
    ('Can I go to the {index_str} one in a wheelchair?', 'The wheelchair access of slot_entity_name is slot_entity_wheelchair_access.', 'entity_index = {index_int}'), 
    ('Tell me about the wheelchair accessibility of that {index_str} place', 'The wheelchair access of slot_entity_name is slot_entity_wheelchair_access.', 'entity_index = {index_int}')
    ]

    # best rating TODO number of top entries is inconsistent
    g = [('What are the best five restaurants?', 'Here are the five highest-rated restaurants: slot_df_name', 'domain = restaurants ; head = 5 ; sortby = rating'),
        ('What are the top 5 restaurants??', 'Here are the five highest-rated restaurants: slot_df_name', 'domain = restaurants ; head = 5 ; sortby = rating'), 
        ('Give me the top-5 of restaurants!', 'The five highest-rated restaurants are: slot_df_name', 'domain = restaurants ; head = 5 ; sortby = rating'), 
        ('Which restaurants have the highest rating?', 'Here are the five highest-rated restaurants: slot_df_name', 'domain = restaurants ; head = 5 ; sortby = rating'), 
        ('Do you know which restaurants are highest rated?', 'Here are the five highest-rated restaurants: slot_df_name', 'domain = restaurants ; head = 5 ; sortby = rating'), 
        ("I'm interested which restaurants are best rated", 'Here are the five highest-rated restaurants: slot_df_name', 'domain = restaurants ; head = 5 ; sortby = rating')
        ]

    # best rating filtered by cuisine
    h = [
        ('What are the best {restaurant_cuisine} restaurants in town?', 'The three highest-rated {restaurant_cuisine} restaurants are: slot_df_name', 'domain = restaurants ; head = 3 ; sortby = rating; cuisine = {restaurant_cuisine}'), 
        ('What are the top 3 restaurants that serve {restaurant_cuisine} food', 'Here are the three highest-rated {restaurant_cuisine} restaurants: slot_df_name', 'domain = restaurants ; head = 3 ; sortby = rating; cuisine = {restaurant_cuisine}'),
        ('Give me the top-3 {restaurant_cuisine} restaurants!', 'The three highest-rated {restaurant_cuisine} restaurants are: slot_df_name', 'domain = restaurants ; head = 3 ; sortby = rating; cuisine = {restaurant_cuisine}'), 
        ('Which {restaurant_cuisine} restaurants have the highest rating?', 'Here are the three highest rated restaurants: slot_df_name', 'domain = restaurants ; head = 3 ; sortby = rating; cuisine = {restaurant_cuisine}'), 
        ('Do you know which {restaurant_cuisine} restaurants are highest rated?', 'Here are the three highest-rated {restaurant_cuisine} restaurants: slot_df_name', 'domain = restaurants ; head = 3 ; sortby = rating; cuisine = {restaurant_cuisine}'), 
        ('What is the best restaurant that serves {restaurant_cuisine} cuisine?', 'Here are the three highest-rated {restaurant_cuisine} restaurants: slot_df_name', 'domain = restaurants ; head = 3 ; sortby = rating; cuisine = {restaurant_cuisine}')
        ]

    # TODO most expensive ones
    i = [
        ('What are the most expensive restaurants?', 'Here is a list of the most expensive restaurants: slot_df_name', 'domain = restaurants ; price_level = 3'),
        ('I want to eat in a really expensive restaurant. Can you show me some?', 'Sure. These restaurants fall in the category expensive: slot_df_name', 'domain = restaurants ; price_level = 3'),
        ('Give me a list of the most expensive restaurants!', 'The list of expensive restaurants includes: slot_df_name', 'domain = restaurants ; price_level = 3'),
        ('Suggest me some of the most expensive restaurants?', 'These belong to the most expensive restaurants: slot_df_name', 'domain = restaurants ; price_level = 3'), 
        ('Can you show me the most expensive restaurants?', 'Yes, these are the most expensive ones: slot_df_name', 'domain = restaurants ; price_level = 3')
        ]


    # TODO cheapest ones
    j = [('What are the cheapest restaurants?', 'Here is a list of the cheapest restaurants: slot_df_name', 'domain = restaurants ; price_level = 1'),
        ('I need to save money. Can you suggest me some restaurants?', 'If you want to save money you could be interested in these cheap restaurants: slot_df_name', 'domain = restaurants ; price_level = 1'),
        ('List me the cheapest restaurants you know?', 'Among the cheapest restaurants we have: slot_df_name', 'domain = restaurants ; price_level = 1'),
        ('Do you have any suggestions for a cheap restaurants?', 'I could suggest you these cheap restaurants: slot_df_name', 'domain = restaurants ; price_level = 1'),
        ('Show me a list of the cheapest restaurants!', 'Here is a list of some of the cheapest restaurants: slot_df_name', 'domain = restaurants ; price_level = 1')]


    # TODO only with wheelchair access
    k = [('Show me restaurants with an entrance accessible by wheelchair?', 'This is a list contains restaurants with an entrance accessible by wheelchair: slot_df_name', 'domain = restaurants ; wheelchair_access = TRUE'),
        ('Can you show me restaurants I can enter with a wheelchair?', 'These are restaurants you could enter with a wheelchair: slot_df_name', 'domain = restaurants ; wheelchair_access = TRUE'),
        ('Do you know restaurants whose entrance is accesible by wheelchair?', 'Here are some restaurants with an entrance suitable for wheelchairs: slot_df_name', 'domain = restaurants ; wheelchair_access = TRUE'),
        ('Are there restaurants with an entrance a wheelchair can pass?', 'Sure. The entrance of these restaurants are accessible for wheelchairs: slot_df_name', 'domain = restaurants ; wheelchair_access = TRUE'),
        ('I am sitting in a wheelchair. Can you suggest me some restaurants I can enter?', 'These are restaurants you can enter with your wheelchair: slot_df_name', 'domain = restaurants ; wheelchair_access = TRUE'),
        ('List me some restaurants I can enter with my wheelchair!', 'If you are sitting in a wheelchair, you could pass the entrance of the these restaurants: slot_df_nam', 'domain = restaurants ; wheelchair_access = TRUE')
        ]
    
    
    histories = []
    
    #1
    histories.append([
        ('I want to go to a restaurant', 'What kind of restaurants do you like? slot_df_cuisine', 'domain = restaurant'),
        ('I want to eat {restaurant_cuisine} food', 'Here are some {restaurant_cuisine} restaurants slot_df_name', 'domain = restaurant ; cuisine = {restaurant_cuisine}'),
        ('What is the address of the {index_str} one?', 'The address of slot_entity_name is slot_entity_address.', 'entity_index = {index_int}'),
        ('Does it have good ratings?', 'The average rating of slot_entity_name based on user reviews is slot_entity_rating out of 5.', ''), 
        ('How expensive is it?', 'The price level of slot_entity_name is slot_entity_price_level out of 3.', ''), 
        ('Can you make a reservation?', 'No, make it yourself. You can call them at slot_entity_phone_number', '')        
    ])
    
    
    #2
    histories.append([
        ('Show me restaurants with an entrance accessible by wheelchair?', 'This is a list contains restaurants with an entrance accessible by wheelchair: slot_df_name', 'domain = restaurants ; wheelchair_access = TRUE'),        
        ('Which restaurants have the highest rating?', 'Here are the five highest-rated restaurants: slot_df_name', 'domain = restaurants ; head = 5 ; sortby = rating'),
        ('How expensive is the {index_str} one?', 'The price level of slot_entity_name is slot_entity_price_level out of 3.', 'entity_index = {index_int}'),
        ('What kind of food do they serve at {restaurant_name}?', 'slot_entity_name serves slot_entity_cuisine food.', 'entity_name = {restaurant_name}'), 
        ('I would like to call them', 'You can call slot_entity_name at slot_entity_phone_number', '')
    ])
    
    
    #3
    histories.append([
        ('Give me a list of the most expensive restaurants!', 'The list of expensive restaurants includes: slot_df_name', 'domain = restaurants ; price_level = 3'),
        ('Can I go to the {index_str} one in a wheelchair?', 'The wheelchair access of slot_entity_name is slot_entity_wheelchair_access.', 'entity_index = {index_int}'), 
        ('Does the {index_str} one have a good rating?', 'The average rating of slot_entity_name based on user reviews is slot_entity_rating out of 5.', 'entity_index = {index_int}'), 
        ('Where is it located?', 'slot_entity_name is located at slot_entity_address.', ''), 
        ('How do I contact them?', 'You can contact slot_entity_name by phone at slot_entity_phone_number', '')
    ])
    
    
    #4
    histories.append([
        ('I am sitting in a wheelchair. Can you suggest me some restaurants I can enter?', 'These are restaurants you can enter with your wheelchair: slot_df_name', 'domain = restaurants ; wheelchair_access = TRUE'),
        ('Does the {index_str} one have a good reputation?', 'Based on user reviews of slot_entity_name, its average rating is slot_entity_rating out of 5.', 'entity_index = {index_int}'), 
        ('Which cuisine can I eat at {restaurant_name}', 'You can try some slot_entity_cuisine cuisine at slot_entity_name.', 'entity_name = {restaurant_name}'), 
        ('What are the prices like at {restaurant_name}?', 'The price level of slot_entity_name is slot_entity_price_level out of 3.', 'entity_name = {restaurant_name}'), 
        ('Do you have more info on {restaurant_name}?', 'You can find out more about slot_entity_name on their website: slot_entity_website', 'entity_name = {restaurant_name}')
    ])
    
    
    #5
    histories.append([
        ('List me the cheapest restaurants you know?', 'Among the cheapest restaurants we have: slot_df_name', 'domain = restaurants ; price_level = 1'),
        ("I'm interested in {restaurant_cuisine} cuisine", 'Some {restaurant_cuisine} restaurants in Stuttgart are slot_df_name', 'domain = restaurant ; cuisine = {restaurant_cuisine}'), 
        ('How do I find this restaurant?', 'You can visit slot_entity_name at slot_entity_address.', ''), 
        ('Can you look up the reviews?', 'According to the reviews, the average rating of slot_entity_name is slot_entity_rating out of 5.', ''), 
        ("What's their website?", 'Their website is slot_entity_website', '')
    ])
    
    
    #6
    histories.append([
        ("I'd like to eat something", 'What kind of food would you like to eat? slot_df_cuisine', 'domain = restaurant'), 
        ('I want to eat {restaurant_cuisine} food', 'Here are some {restaurant_cuisine} restaurants slot_df_name', 'domain = restaurant ; cuisine = {restaurant_cuisine}'),
        ('What is the price level of the {index_str} one?', 'The price level of slot_entity_name is slot_entity_price_level out of 3.', 'entity_index = {index_int}'), 
        ('Tell me the rating of the {index_str} one', 'slot_entity_name is rated slot_entity_rating out of 5.', 'entity_index = {index_int}'), 
        ('Does it have a homepage?', 'Yes, you can visit their homepage at slot_entity_website', '')
    ])


    #7
    histories.append([
        ('What can you tell me about restaurants here in Stuttgart?', 'You can find a range of different cuisines around here. What do you prefer? slot_df_cuisine', 'domain = restaurant'),
        ('List {restaurant_cuisine} restaurants', 'Here is a list of {restaurant_cuisine} restaurants slot_df_name', 'domain = restaurant ; cuisine = {restaurant_cuisine}'), 
        ('Does the {index_str} one have a good rating?', 'The average rating of slot_entity_name based on user reviews is slot_entity_rating out of 5.', 'entity_index = {index_int}'), 
        ('How good is that {index_str} one from the list?', 'slot_entity_name has a rating of slot_entity_rating out of 5.', 'entity_index = {index_int}'), 
        ('Is the {index_str} one any good?', 'It has an average rating of slot_entity_rating out of 5.', 'entity_index = {index_int}'), 
        ('What is its address?', 'The address of slot_entity_name is slot_entity_address.', '')
    ])
    
    
    #8
    histories.append([
        ('Where can i get some {restaurant_cuisine} food?', 'You can get {restaurant_cuisine} food at these restaurants slot_df_name', 'domain = restaurant ; cuisine = {restaurant_cuisine}'),
        ('I am sitting in a wheelchair. Can you suggest me some restaurants I can enter?', 'These are restaurants you can enter with your wheelchair: slot_df_name', 'domain = restaurants ; wheelchair_access = TRUE'),
        ('What are the prices like at {restaurant_name}?', 'The price level of slot_entity_name is slot_entity_price_level out of 3.', 'entity_name = {restaurant_name}'), 
        ('How expensive is {restaurant_name}?', 'The price level of slot_entity_name is slot_entity_price_level out of 3.', 'entity_name = {restaurant_name}'), 
        ('Can you call it for me?', 'I can give you the phone number so you can do it: slot_entity_phone_number', ''), 
    ])
    
    
    #9
    histories.append([
        ('Recommend me a restaurant in Stuttgart', "There are a lot of restaurants, so let's try to narrow it down. What cuisine do you prefer? slot_df_cuisine", 'domain = restaurant'), 
        ('I want to eat {restaurant_cuisine}', 'Here are some {restaurant_cuisine} restaurants slot_df_name', 'domain = restaurant ; cuisine = {restaurant_cuisine}'), 
        ('Does the {index_str} one have a good reputation?', 'Based on user reviews of slot_entity_name, its average rating is slot_entity_rating out of 5.', 'entity_index = {index_int}'), 
        ('How do I find that {index_str} one?', 'You can visit slot_entity_name at slot_entity_address.', 'entity_index = {index_int}'), 
        ('Tell me about the wheelchair accessibility of that {index_str} place', 'The wheelchair access of slot_entity_name is slot_entity_wheelchair_access.', 'entity_index = {index_int}')
    ])
    
    #10
    histories.append([
        ("I'm interested in {restaurant_cuisine} cuisine", 'Some {restaurant_cuisine} restaurants in Stuttgart are slot_df_name', 'domain = restaurant ; cuisine = {restaurant_cuisine}'), 
        ('List me the cheapest restaurants you know?', 'Among the cheapest restaurants we have: slot_df_name', 'domain = restaurants ; price_level = 1'),
        ('Can you show me restaurants I can enter with a wheelchair?', 'These are restaurants you could enter with a wheelchair: slot_df_name', 'domain = restaurants ; wheelchair_access = TRUE'),
        ('How do I get to the {index_str} one on the list?', 'To get to slot_entity_name, you can drive or take public transport to slot_entity_address.', 'entity_index = {index_int}'), 
        ('Where can I read more about it?', "You can visit slot_entity_name's website: slot_entity_website", '')
    ])
    
    #11
    histories.append([
        ('Can you show me the most expensive restaurants?', 'Yes, these are the most expensive ones: slot_df_name', 'domain = restaurants ; price_level = 3'),
        ('Is the {index_str} one any good?', 'It has an average rating of slot_entity_rating out of 5.', 'entity_index = {index_int}'), 
        ('Tell me the rating of the {index_str} one', 'slot_entity_name is rated slot_entity_rating out of 5.', 'entity_index = {index_int}'), 
        ('Can you make a reservation?', 'No, make it yourself. You can call them at slot_entity_phone_number', ''), 
        ('Give me the directions to get there', 'The address of slot_entity_name is slot_entity_address.', '')
    ])
       
    #12   
    histories.append([
        ('Give me {restaurant_cuisine} restaurants', 'Here are {restaurant_cuisine} restaurants slot_df_name', 'domain = restaurant ; cuisine = {restaurant_cuisine}'), 
        ('Show me a list of the cheapest restaurants!', 'Here is a list of some of the cheapest restaurants: slot_df_name', 'domain = restaurants ; price_level = 1'),
        ('Look up the reviews for {restaurant_name}', 'According to the reviews, the average rating of slot_entity_name is slot_entity_rating out of 5.', 'entity_name = {restaurant_name}'), 
        ("What's the website of {restaurant_name}?", 'Their website is slot_entity_website', 'entity_name = {restaurant_name}'), 
        ('I would like to call them', 'You can call slot_entity_name at slot_entity_phone_number', '')
    ])
       
       
    #13  
    histories.append([
        ('I need to save money. Can you suggest me some restaurants?', 'If you want to save money you could be interested in these cheap restaurants: slot_df_name', 'domain = restaurants ; price_level = 1'),
        ('What are the prices there?', 'The price level of slot_entity_name is slot_entity_price_level out of 3.', ''), 
        ('What is the address of {restaurant_name}?', 'The address of slot_entity_name is slot_entity_address.', 'entity_name = {restaurant_name}'), 
        ('How do I contact them?', 'You can contact slot_entity_name by phone at slot_entity_phone_number', ''), 
        ('Do you have more info on it?', 'You can find out more about slot_entity_name on their website: slot_entity_website', '')

    ])
    
    
    #14   
    histories.append([
        ('Do you know any restaurants?', 'Sure. Which cuisines should the restaurant serve? slot_df_cuisine', 'domain = restaurant'),
        ('Give me the top-3 {restaurant_cuisine} restaurants!', 'The three highest-rated {restaurant_cuisine} restaurants are: slot_df_name', 'domain = restaurants ; head = 3 ; sortby = rating; cuisine = {restaurant_cuisine}'), 
        ('What is the rating of {restaurant_name}?', 'slot_entity_name has a rating of slot_entity_rating out of 5', 'entity_name = {restaurant_name}'), 
        ('How much does it cost to eat at {restaurant_name}?', 'The price level of slot_entity_name is slot_entity_price_level out of 3.', 'entity_name = {restaurant_name}'), 
        ("Can I go there if I'm in a wheelchair?", 'The wheelchair access of slot_entity_name is slot_entity_wheelchair_access.', ''),
        ('Give me the directions to get there', 'The address of slot_entity_name is slot_entity_address.', '')
    ])
    
    
    #15
    histories.append([
        ('Where can i grab something to eat?', 'What cuisines are you interested in? slot_df_cuisine', 'domain = restaurant'), 
        ("I'm really craving {restaurant_cuisine} food right now", 'Here are some {restaurant_cuisine} restaurants for you: slot_df_name', 'domain = restaurant ; cuisine = {restaurant_cuisine}'),
        ('Are there restaurants with an entrance a wheelchair can pass?', 'Sure. The entrance of these restaurants are accessible for wheelchairs: slot_df_name', 'domain = restaurants ; wheelchair_access = TRUE'),
        ('Does the {index_str} one have a good rating?', 'The average rating of slot_entity_name based on user reviews is slot_entity_rating out of 5.', 'entity_index = {index_int}'), 
        ('What are the prices like at {restaurant_name}?', 'The price level of slot_entity_name is slot_entity_price_level out of 3.', 'entity_name = {restaurant_name}')
    ])      
        
    
    
    return histories
