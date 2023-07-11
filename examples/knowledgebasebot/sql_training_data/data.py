from parametrize import parametrize, parametrize_all
from to_soloist_format import to_soloist_format
import json

ask_for_museum_about = parametrize({
    "user": "%(user_input)s",
    "belief": "df = domains['museum'].query('about == \"%(about)s\"') ; row = None ; names = df['name'].tolist()",
    "system": "Here are some museums about %(about)s {names}",
    }, 
    {"user_input": [
        "I would like to see a museum about %(about)s",
        "I want to go to a museum about %(about)s",
        "I'd like to visit a %(about)s museum",
        "Please recommend some %(about)s museums for me",
        "are there any good museums about %(about)s in Stuttgart",
        "Show me a list of museums with the topic %(about)s",
        "Recommend some %(about)s museums for me",
        "What museums are in Stuttgart, that are about %(about)s",
        "Do you know of any good %(about)s museums here?"]
    }
)

_ask_for_attribute_by_name = parametrize({
    "user": "%(user)s",
    "belief": "row = df.query('name == \"%(name)s\"') ; %(key)s = row['%(key)s']",
    "system": "The %(attribute)s of the %(name)s is {%(key)s}"
    },
    {
        "user": [
            "What is the %(attribute)s of the %(name)s",
            "Could you tell me the %(attribute)s of the %(name)s",
            "Regarding the %(name)s what is its %(attribute)s",
            "Would you be so kind to inform me about the %(attribute)s of the %(name)s",
            "Do tell me what the %(attribute)s of the %(name)s is",
            "Tell me the %(attribute)s of the %(name)s",
            "What's the %(attribute)s of %(name)s",
            "What is %(name)s's %(attribute)s",
            "What is the of %(attribute)s of the %(name)s"
        ]
    }
)

ask_for_attribute_by_name = parametrize_all(
    _ask_for_attribute_by_name,
    {
        "name, attribute, key": [
            ("Oblomov", "address", "address"),
            ("L'Osteria", "phone number", "phone_number"),
            ("Gutenberg", "wine press", "wine_press"),
            ("Ikea", "parking lot size", "parking_lot_size"),
            ("Mc Donald's", "annual revenue", "annual_revenue"),
            ("Titanic", "passenger count", "passenger_count"),
            ("Steel", "hardness", "hardness"),
            ("Sun", "diameter", "diameter"),
            ("Willies Tower", "height", "height"),
            ("garage sale", "date", "date")
        ]
    }, max_len=20
)

_ask_for_attribute_by_index = parametrize({
    "user": "%(user)s",
    "belief": "row = df.iloc[%(index_num)s] ; %(key)s = row['%(key)s'] ; name = row['name']",
    "system": "The %(attribute)s of the {name} is {%(key)s}"
    },
    {
        "user": [
            "What is the %(attribute)s of the %(index_name)s one?",
            "What's the %(attribute)s of the %(index_name)s?",
            "Tell me the %(attribute)s of the %(index_name)s %(domain)s",
            "Can you lookup the %(attribute)s of the %(index_name)s %(domain)s for me please?",
            "I want to know the %(attribute)s of the %(index_name)s"
        ]
    }
)

ask_for_attribute_by_index = parametrize_all(
    _ask_for_attribute_by_index,
    {
        "attribute, key, domain": [
            ("duration", "duration", "movie"),
            ("author", "author", "book"),
            ("trainer", "trainer", "team"),
            ("driver", "driver", "car"),
            ("size", "size", "building"),
            ("elevation", "elevation", "view")
        ],
        "index_text, index_num": [
            ("first", 0),
            ("second", 1),
            ("third", 2),
            ("fourth", 3),
            ("fifth", 4),
            ("last", -1),
            ("second last", -2)
        ]
    }, max_len=20
)

ask_for_restaurant_with_cuisine = parametrize({
    "user": "%(user_input)s",
    "belief": "df = domains['restaurant'].query('cuisine == \"%(cuisine)s\"') ; names = df['name'].tolist()",
    "system": "These are restaurants that serve %(cuisine)s food {names}",
    },
    {
        "user_input": [
            "I would like to eat some %(cuisine)s food",
            "I could really go for some %(cuisine)s food right now",
            "Do you know some places that serve %(cuisine)s food?"
        ]
    })

ask_for_museum = parametrize({
    "user" : "%(user)s",
    "belief" : "df = domains['museum'] ; about = df['about'].unique()",
    "system" : "I know museums about the following topics {about}"
    },
    {
        "user": [
            "I would like to go to a museum",
            "What kind of museums do you know of?"
        ]
    })


data = [
    *parametrize_all(ask_for_museum_about, {
        "about": ['art', 'history', 'war', 'cars']}, max_len=20),
    *parametrize_all(ask_for_restaurant_with_cuisine, {
        "cuisine": ["mexican", "indian", "german", "swedish", "chinese", "american", "italian"]}, max_len=20),
    *ask_for_attribute_by_name,
    *ask_for_attribute_by_index
]

with open('data.json', 'w+') as f:
    data = list(map(to_soloist_format, data))
    json.dump(data, f, indent=4)
