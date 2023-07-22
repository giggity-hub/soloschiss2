from utils.unique_random import UniqueRandom
#from domains.domains import load_domains_dict, load_domain_sampler

def main(domain_sampler, parametrize):
    attributes_and_col_name = [
        ('number of steps', 'number_of_steps'),
        ('height')
    ]


    # Include 1 question for every column name in our datasets
    # Also include attributes which are not in the dataset. hopefully this will lead to better generalization
    # DO NOT INCLUDE SYNONYMS: topic should not be recognized as the about column and instead as the topic column
    # We can resolve synonyms in the chatbot. this makes it easier for the model
    user_system = [
        ('What is the number of steps of the %(entity_mention)s', 
            'The slot_entity_name has slot_entity_number_of_steps steps'),
        ('How tall is the %(entity_mention)s', 
            'The slot_entity_name is slot_entity_tall tall'),
        ('What is the rating of the %(entity_mention)s',
            'The rating of the slot_entity_name is slot_entity_rating'),
        ('Please give me the phone number of the %(entity_mention)s',
            'The phone number of the slot_entity_name is slot_entity_phone_number'),
        ('Could you provide me with the url of the %(entity_mention)s',
            'The url of the slot_entity_name is slot_entity_url')
    ]

    # Extend the following list of entity mentions
    
    # Der domain_sampler hat eine funktion um einen random index zu bekommen
    # domain_sampler['index'].sample() gibt z.b. ('first', 1)
    # 1.) fuege zu dem domain sampler eine sample methode hinzu sodass du eine zufaellige domain bekommnst
    # 2.) fuege zu dem domain sampler eine sample methode hinzu sodass du einen zufaelligen namen bekommst
    # Den domain sampler findest du in domains.domains

    # Mentions can be of five types (unless i forgot some)
    # generate mentions of every type. Utilize the domain sampler and the index, domain and name sample methods
    entity_mentions_bs_and_type = [
        # type 1: just the name
        ('Hotalo', 'Hotalo', 'name'),
        # type two: index + 'one'
        ('first one', 0, 'index'),
        # type three: just index
        ('last', -1, 'index'),
        # type four: index + domain name
        ('first restaurant', 0, 'index'),
        # type five name + domain name
        ('StadtPalais museum', 'StadtPalais', 'name')
    ]
    # Below are two functions which generate mentions of a given type
    def generate_type_five(n): # not sure if it works
        res = []
        for i in range(n):
            # assuming that you have defined a "name" sampler in domains.domains
            rand_name = domain_sampler['name'].sample()
            rand_domain = domain_sampler['domain'].sample()
            res.append((f'{rand_name} {rand_domain}', rand_name, 'name'))
        return res

    def generate_type_one(n): # works
        res = []
        for i in range(n):
            rand_name = domain_sampler['name'].sample()
            res.append((rand_name, rand_name, 'name'))
        return res

    def generate_type_two(n): # works
        res = []
        for i in range(n):
            index_str, index_int = domain_sampler['index'].sample()
            res.append((index_str + ' one', index_int, 'index'))
        return res
    
    def generate_type_three(n): #works
        res = []
        for i in range(n):
            index_str, index_int = domain_sampler['index'].sample()
            res.append((index_str, index_int, 'index'))
        return res

    def generate_type_four(n): #works
        res = []
        for i in range(n):
            index_str, index_int = domain_sampler['index'].sample()
            rand_domain = domain_sampler['domain'].sample()
            res.append((index_str + " " + rand_domain, index_int, 'index'))
        return res

    
    
    # Now you also need to write a function which constructs a belief state given a 
    res = []



    """
    ################
    no_examples = 3
    response1 = generate_type_one(no_examples)
    response2 = generate_type_two(no_examples)
    response3 = generate_type_three(no_examples)
    response4 = generate_type_four(no_examples)
    response5 = generate_type_five(no_examples)
    print("response1:", response1)
    print("response2:", response2)
    print("response3:", response3)
    print("response4:", response4)
    print("response5:", response5)
    """

"""
domains_dict = load_domains_dict()
domain_sampler = load_domain_sampler(domains_dict=domains_dict)
main(domain_sampler=domain_sampler, parametrize=None)
"""