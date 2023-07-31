def main():
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