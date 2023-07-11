from parametrize import parametrize, parametrize_all
from to_soloist_format import to_soloist_format
import json

ask_for_museum_about = parametrize({
    "user": "%(user_input)s",
    "belief": "df = domains['museum'].query('about == \"%(about)s\"') ; names = df['name'].tolist()",
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
        "about": ['art', 'history', 'war', 'cars']}),
    *parametrize_all(ask_for_restaurant_with_cuisine, {
        "cuisine": ["mexican", "indian", "german", "swedish", "chinese", "american", "italian"]})
]

with open('data.json', 'w+') as f:
    data = list(map(to_soloist_format, data))
    json.dump(data, f, indent=4)
