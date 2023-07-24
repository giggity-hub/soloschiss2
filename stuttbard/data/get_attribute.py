from utils.unique_random import UniqueRandom
#from domains.domains import load_domains_dict, load_domain_sampler

def main(domain_sampler, parametrize):

    # Add some more user_system examples here
    ask_for_single_attr_without_mention = parametrize({
        'belief': '',
        'user_system': [
            ('Give me the address of that place',
                'The address of the slot_entity_name is slot_entity_address'),
            ('Where is it located?',
                'The slot_entity_name is located at slot_entity_address'),
            ('Tell me the sheesh of it',
                'The sheesh of the slot_entity_name is slot_entity_sheesh'),
            ('Lookup the price range of that place',
                'The price range of the slot_entity_name is slot_entity_price_range'),
            ('What is the influx of it?',
                'The influx of the slot_entity_name is slot_entity_influx'),
            ('How much does it weigh?',
                'The slot_entity_name weighs slot_entity_weight'),
            ('Can you give me the house number?',
                'The house number of the slot_entity_name is slot_entity_house_number'),
            ('In which area is it?',
                'The slot_entity_name is in the slot_entity_area area'),
            ('Which district is it in?',
                'The slot_entity_name is in the slot_entity_district district'),
            ('Is it wheelchair accessible?', 
                'The slot_entity_name is slot_entity_wheelchair_access'),
            ('Do they have student discounts?',
                'The slot_entity_name has slot_entity_student_discounts'),
            ('Do they offer free wifi?',
                'The slot_entity_name offers slot_entity_free_wifi'),
            ('In what year was it build?',
                'The slot_entity_name was build in slot_entity_year_build'),
            ('What is the average rating of that place?',
                'The average rating of the slot_entity_name is slot_entity_average_rating'),
            ('What is its height?',
                'The height of the slot_entity_name is slot_entity_height'),
            ('And what is the diameter?',
                'The diameter fo the slot_entity_name is slot_entity_diameter')
        ]
    })

    # Add some more user_system examples here
    ask_for_single_attr_by_mention = parametrize({
        'belief': '%(mention_belief_state)s',
        'samplers': {
            'entity_mention, mention_belief_state': domain_sampler['entity']
        },
        'user_system': [
        ('What is the name of the %(entity_mention)s?',
            'The name of the slot_entity_name is slot_entity_name'),
        ('I want to know which area the %(entity_mention)s is in',
            'The slot_entity_name is in the slot_entity_area area'),
        ('What is the number of steps of the %(entity_mention)s?', 
            'The slot_entity_name has slot_entity_number_of_steps steps'),
        ('How many steps does the %(entity_mention)s have?',
            'The slot_entity_name has slot_entity_number_of_steps steps'),
        ('Tell me the length of the %(entity_mention)s',
            'The length of the slot_entity_name is slot_entity_length'),
        
        ('What is the price of the %(entity_mention)s',
            'The price of the slot_entity_name is slot_entity_price'),
        ('I demand that you tell me the purpose of the %(entity_mention)s',
            'The purpose of the slot_entity_name is slot_entity_purpose'),
        ('Can you find out what the annual revenue of the %(entity_mention)s is please?',
            'The annual revenue of the slot_entity_name is slot_entity_annual_revenue'),
        ('Look up the halflife time of the %(entity_mention)s',
            'The halflife time of the slot_entity_name is slot_entity_half_life_time'),
        ('Find out what the sugar content of the %(entity_mention)s is for me',
            'The sugar content of the slot_entity_name is slot_entity_sugar_content'),
        
        ('How tall is the %(entity_mention)s?', 
            'The slot_entity_name is slot_entity_tall tall'),
        ('What is the rating of the %(entity_mention)s?',
            'The rating of the slot_entity_name is slot_entity_rating'),
        ('Please give me the phone number of the %(entity_mention)s',
            'The phone number of the slot_entity_name is slot_entity_phone_number'),
        ('Could you provide me with the url of the %(entity_mention)s',
            'The url of the slot_entity_name is slot_entity_url'),
        ('Do you know the size of the %(entity_mention)s?',
            'The size of the slot_entity_name is slot_entity_size'),
        ('What is the maximum occupancy of the %(entity_mention)s?',
            'The maximum occupancy of the slot_entity_name is slot_entity_maximum_occupancy'),
        ('What is the loudness of the %(entity_mention)s?',
            'The loudness of the slot_entity_name is slot_entity_loudness'),
        ('Can you please tell me the address of the %(entity_mention)s',
            'The address of the slot_entity_name is slot_entity_address'),
        ('And what is the duration of the %(entity_mention)s?',
            'The duration of the slot_entity_name is slot_entity_duration'),
    ]
    })
    
    return [*ask_for_single_attr_by_mention, *ask_for_single_attr_without_mention]
