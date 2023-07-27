def main():

    histories = []
    
    histories.append([
        ("List me some %(museum_about)s museums in Stuttgart.", 
            "Sure, here is a list of museums about %(museum_about)s: slot_df_name.", 
            "domain = museum ; about = %(museum_about)s"),
        ("More specific I am interested in museums with the topic %(museum_about_specific)s.", 
            "The list of museums about %(museum_about_specific)s includes: slot_df_name.", 
            "about_specific = %(museum_about_specific)"),
        ("Can you give me the phone number of the %(index_str)s one", 
            "The slot_entity_name museum has the phone number slot_entity_phone_number", 
            "entity_index = %(index_int)s"),
        ("What is the adress of this museum again?", 
            "The museum has the adress: slot_entity_address", 
            ""),
        ("Then give me the google plus code of this museum.", 
            "The slot_entity_name museum has the international google plus code slot_entity_plus_code.", 
            "")
    ])



    histories.append([
        ("What topics do the museums in Stuttgart have?", 
            "Stuttgart contains museums about these topics: slot_df_about", 
            "domain = museum"),
        ("I want to visit a museum in the area %(museum_area)s", 
            "In the area %(museum_area)s we have museums about the topics slot_df_about", 
            "area = %(museum_area)s"),
        ("Give me the highest rated museum.", 
            "The slot_entity_name museum has with slot_entity_rating the highest rating in this area.", 
            "sortby = rating ; head = 1"),
        ("Where is this museum?", 
            "The slot_entity_name museum is located at the adress slot_entity_address.", 
            ""),
        ("Does the museum have an accessible entrance for wheelchair users", 
            "The museum has an accesible entrance for wheelchair users is slot_entity_wheelchair_access", 
            "")    
    ])  



    histories.append([
        ("I am interested in the %(museum_name)s museum in Stuttgart.", 
            "For the slot_entity_name museum I can give you information on these properties: df_columns",
            "domain = museum ; name = %(museum_name)s"),
        ("What is the adress of the %(museum_name)s museum in Stuttgart?", 
            "The slot_entity_name museum has the adress slot_entity_address",
            ""),
        ("In which street is the %(museum_name)s museum?", 
            "You can find the slot_entity_name museum in the slot_entity_street street.",
            ""),
        ("Tell me the house number of the %(museum_name)s museum!", 
            "The house number is slot_entity_house_number.",
            ""),
        ("Show me more information about the %(museum_name)s museum in Stuttgart!", 
            "For more information about the museum I can give you the website link slot_entity_website and the google plus code slot_entity_plus_code",
            "")
    ])
    
    
    
    histories.append([
        ("List me the museum in Stuttgart according to their rating.", 
            "Here is the list of museums sorted by their google ratings: slot_df_name",
            "domain = museum ; sortby = rating"),
        ("What is the rating of the %(index_str)s one?", 
            "The %(index_str)s museum called slot_entity_name has a google rating of slot_entity_rating.",
            "entity_index = %(index_int)s"),
        ("Is the museum for children?", 
            "The suitability of the slot_entity_name museum for children is: slot_entity_children.",
            ""),
        ("What is the theme of the %(museum_name)s museum?", 
            "slot_entity_about is the topic of the slot_entity_name museum",
            ""),
        ("Can you give me the adress of this museum?", 
            "Sure, the %(museum_name)s museum can be found at slot_entity_adress.",
            "")
    ])
    
    
    
    histories.append([
        ("Are there any museums suitable for children?", 
            "Here are suitable museums for children: slot_df_name",
            "domain = museum ; for_children = 1"),
        ("Show me the topic of the first %(number_str)s museums!", 
            "These are the topics of the first %(number_str)s museums: slot_df_about",
            "head = %(number_int)s"),
        ("How popular is the %(index_str)s museum?", 
            "On google maps the slot_entity_name museum achieved an average rating of slot_entity_rating.",
            "entity_index = %(index_int)s"),
        ("Do you know the location of the museum?", 
            "The museum has the house number slot_entity_house_number of the slot_entity_street in the area slot_entity_area.",
            ""),
        ("How can I contact the museum?", 
            "You can reach the slot_entity_name museum under slot_entity_phone_number.",
            "")
    ])
    
    
   
    return histories