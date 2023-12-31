def main():

    histories = []

    histories.append([
        ("Are there any staeffeles in the {stairs_area} area?", 
            "Here are staeffeles in {stairs_area} slot_df_name", 
                "domain = stairs ; area = {stairs_area}"),
        ("Tell me the height of the {index_str} one please",
            "The slot_entity_name has a height of slot_entity_height",
                "entity_index = {index_int}"),
        ("How high is the {stairs_name} ?",
            "The slot_entity_name has a height of slot_entity_height",
                "entity_name = {stairs_name}"),
        ("What else can you tell me about Stairs",
            "You can ask me about the following properties of stairs df_columns"),
        ("Tell me how long the {index_str} one is please",
            "The slot_entity_name has a length of slot_entity_height",
                "entity_index = {index_int}"),
        ("How high is it?",
            "The slot_entity_name has a height of slot_entity_height"),
        ("I want to know what the five longest staeffeles in {stairs_area} are",
                "Here are the five longest stairs in {stairs_area}. slot_df_name",
                    "domain = stairs ; head = 5 ; sortby = length ; area = {stairs_area}"),
        ("How many steps does the {stairs_name} have?",
            "The slot_entity_name has slot_entity_number_of_steps steps",
                "entity_name = {stairs_name}"),
        ("Who was the {stairs_name} named after?",
            "The slot_entity_name was named after slot_entity_named_after",
                "entity_name = {stairs_name}"),
    ])

    histories.append([
        ("I want to see some of the famous Stuttgarter stairs",
            "In which area would you like to look for staeffeles? i know some in slot_df_area",
                "domain = stairs"),
        ("Please show me some staeffeles in {stairs_area}", 
            "Here are staeffeles in {stairs_area} slot_df_name",
                "domain = stairs ; area = {stairs_area}"),
        ("Nevermind, I want to go to the {stairs_area} area",
            "Here are staeffeles in {stairs_area} slot_df_name",
                "area = {stairs_area}"),
        ("I want to know who the {index_str} of those was named after",
            "The slot_entity_name was named after slot_entity_named_after",
                "entity_index = {index_int}"),
        ("Tell me how long it is",
            "The slot_entity_name has a length of slot_entity_height"),
        ("Wha is the number of steps of the {stairs_name}?",
            "The slot_entity_name has slot_entity_number_of_steps steps",
                "entity_name = {stairs_name}"),
        ("Tell me the length of the {stairs_name}",
            "The slot_entity_name has a length of slot_entity_length",
                "entity_name = {stairs_name}"),
        ("How many steps does it have?",
            "The slot_entity_name has slot_entity_number_of_steps steps"),
    ])

    histories.append([
        ("Show me some staeffeles please",
            "In which area would you like to look for staeffeles? i know some in slot_df_area",
                "domain = stairs"),
        ("I'd like to go to the {stairs_area}", 
            "Here are staeffeles in {stairs_area} slot_df_name",
                "area = {stairs_area}"),
        ("How high is the {index_str} of those?",
            "The slot_entity_name has a height of slot_entity_height",
                "entity_index = {index_int}"),
        ("Can you tell me the number of steps of that one?",
            "The slot_entity_name has slot_entity_number_of_steps steps"),
        ("How did the {stairs_name} come to its name?",
            "The slot_entity_name was named after slot_entity_named_after",
                "entity_name = {stairs_name}"),
        ("I want to know which stair has the most steps",
            "With slot_entity_number_of_steps steps, the slot_entity_name has the most steps",
                "domain = stairs ; sortby = number_of_steps; entity_index = 0"),
        ("Which part of town is it in?",
            "The slot_entity_name is in the slot_entity_area area")
    ])

    histories.append([
        ("Do you know any good stairs to climb?",
            "In which area would you like to look for staeffeles? i know some in slot_df_area",
                "domain = stairs"),
        ("Show me the ones in {stairs_area}",
            "Here are staeffeles in {stairs_area} slot_df_name",
                "area = {stairs_area}"),
        ("Can you tell me what the five highest stairs are in that area?",
            "Here are the five highest stairs in slot_area. slot_df_name",
                "domain = stairs ; head = 5 ; sortby = height"),
        ("What's the length of the {index_str} one?",
                "The slot_entity_name has a length of slot_entity_length",
                    "entity_index = {index_int}"),
        ("Do you know who the {index_str} was named after?",
            "The slot_entity_name was named after slot_entity_named_after",
                "entity_index = {index_int}"),
        ("Look up how many steps the {index_str} set of stairs has please",
            "The slot_entity_name has slot_entity_number_of_steps steps",
                "entity_index = {index_int}"),
        ("Which stair has the most number of steps?",
            "With slot_entity_number_of_steps steps, the slot_entity_name has the most steps",
                "domain = stairs ; sortby = number_of_steps; entity_index = 0"),
    ])

    histories.append([
        ("Tell me about the staeffeles in Stuttgart",
            "In which area would you like to look for staeffeles? i know some in slot_df_area",
                "domain = stairs"),
        ("In the {stairs_area} area",
            "Here are some staeffeles in {stairs_area} slot_df_name",
                "area = {stairs_area}"),
        ("What is the height of the {stairs_name} ?",
            "The slot_entity_name has a height of slot_entity_height",
                "entity_name = {stairs_name}"),
        ("Show me the five highest stairs in {stairs_area}",
            "Here are the five highest stairs in {stairs_area}. slot_df_name",
                "domain = stairs ; head = 5 ; sortby = height; area = {stairs_area}"),
        ("Do you know how many steps the {index_str} one has?",
            "The slot_entity_name has slot_entity_number_of_steps steps",
                "entity_index = {index_int}"),
        ("Who gave it it's name?",
            "The slot_entity_name was named after slot_entity_named_after"),
        ("Tell me which staeffeles has the most steps",
            "With slot_entity_number_of_steps steps, the slot_entity_name has the most steps",
                "domain = stairs ; sortby = number_of_steps; entity_index = 0"),
        ("What's it's length?",
            "The slot_entity_name has a length of slot_entity_length"),
        ("In what part of town is it?",
            "The slot_entity_name is in the slot_entity_area area"),
    ])

    histories.append([
        ("Do you know where i can find any staeffeles?",
            "In which area would you like to look for staeffeles? i know some in slot_df_area",
                "domain = stairs"),
        ("I want to go to a staeffele in {stairs_area}", 
            "Here are staeffeles in {stairs_area} slot_df_name",
                "domain = stairs ; area = {stairs_area}"),
        ("Show me the stair with the most steps",
            "With slot_entity_number_of_steps steps, the slot_entity_name has the most steps",
                "domain = stairs ; sortby = number_of_steps; entity_index = 0"),
        ("Which stairs in {stairs_area} belong to the 5 highest?",
            "Here are the five highest stairs in {stairs_area}. slot_df_name",
                "domain = stairs ; head = 5 ; sortby = height; area = {stairs_area}"),
        ("Now i want to see some in {stairs_area} please",
            "Here are some staeffeles that fit your description slot_df_name",
                "area = {stairs_area}"),
        ("How long is the {stairs_name}?",
            "The slot_entity_name has a length of slot_entity_height",
                "entity_name = {stairs_name}"),
        ("Tell me it's height",
            "The slot_entity_name has a height of slot_entity_height"),
        ("Who was that stair set named after?",
            "The slot_entity_name was named after slot_entity_named_after"),
    ])

    return histories