from parametrize import parametrize, parametrize_all

def d(user, belief, system):
    return {
        "user": user,
        "system": system,
        "belief": belief,
    }

data = [
    # Wants to visit a museum about something
    parametrize

    parametrize({
        "user": "One about %(about)s please",
        "belief": "df = df.query('about == \"%(about)s\"') ; names = df['name'].tolist()",
        "system": "Here are some museums about %(about)s {names}"
    }, {'about': ['history', 'art', 'war', 'tanks', 'music', 'culture', 'ethnology']}),
    {
        "user": "Which of those have a discount for students?",
        "belief": "names = df.query('student_discount == True')",
        "system": "These art museums all offer a discount for students {names}"
    },
    parametrize({
        "user": "Very well. I would like to go to the %(name)s museum. What is the address?",
        "belief": "row = df.query('name == \"%(name)s\"').iloc[0] ; address = row['address']",
        "system": "You can find the Gugelhupf museum at {address}"
    }, {"name": ['Gugelhupf', 'Staatsgallerie', 'Heimatland', 'Koerperwelten']}),

    {
        "user" : "I would like to visit a history museum",
        "belief" : "df = domains['museum'].query('about == \"history\"') ; names = df['name'].tolist()",
        "system" : "These are museums about history {names}"
    },
        {
            "user": "Nevermind, i'd rather go to a museum about tanks",
            "belief": "df = domains['museum'].query('about == \"tanks\"') ; names = df['name'].tolist()",
            "system": "Here are museums about tanks {names}"
        },
        {
            "user": "What are the opening hours of the Panzerland?",
            "belief": "row = df.query('name == \"Panzerland\"').iloc[0] ; opening_hours = row['opening_hours']",
            "system": "The opening hours of the Panzerland are {opening_hours}"
        },
        {
            "user": "What is the address?",
            "belief": "address = row['address'] ; name = row['name']",
            "system": "The address of the {name} is {address}"
        },
        {
            "user": "What are the url and the phone number of the third one?",
            "belief": "row = df.iloc[4] ; name = row['name'] ; url = row['url'] ; phone_number = row['phone_number']",
            "system": "The url of the {name} is {url} and the phone number is {phone_number}"
        }
    ],
    [
        {
            "user": "Recommend some restaurants for me",
            "belief": "df = domains['restaurant'] ; cuisines = df['cuisine'].unique()",
            "system": "Which type of food do you like? Choose one of these cuisines {cuisines}"
        },
        {
            "user": "I want to eat chinese today",
            "belief": "df = domains['restaurant'].query('cuisine == \"chinese\"') ; names = df['name'].tolist()",
            "system": "Here are some chinese restaurants you might like {names}"
        },
        {
            "user": "The Yellow River sounds nice. Where can i find it?",
            "belief": "row = df.query('name == \"Yellow River\"') ; address = row['address']",
            "system": "You can find the Yellow River at {address}"
        },
        {
            "user": "And the second one, what is the address of that place?",
            "belief": "row = df.iloc[1] ; name = row['name'] ; address = row['address']",
            "system": "The address of the {name} is {address}"
        }
    ],
    [
        {
            "user": "Hello. What can you talk about?",
            "belief": "domain_keys = domains.keys()",
            "system": "I can talk to you about places in Stuttgart like {domain_keys}"
        },
        {
            "user": "I would like to go to a restaurant",
            "belief": "df = domains['restaurant'] ; cuisines = df['cuisine'].unique()",
            "system": "What kind of cuisine are you looking for? I know of the following {cuisines}"
        },
        {
            "user": "I want to eat mexican food",
            "belief": "df = domains['restaurant'].query('cuisine == \"mexican\"') ; names = df['name'].tolist()",
            "system": "Here are some mexican restaurants i know of {names}"
        },
        {
            "user": "What is the address of the first one?",
            "belief": "row = df.iloc[0] ; address = row['address'] ; name = row['name']",
            "system": "The address of the {name} is {address}"
        },
        {
            "user": "Does the Salitos have free wifi?",
            "belief": "row = df.query('name == \"Salitos\"').iloc[0] ; free_wifi = row['free_wifi']",
            "system": "The value of 'free_wifi' for the Salitos is {free_wifi}"
        }
    ]

]