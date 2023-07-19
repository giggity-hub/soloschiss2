from googleplaces import GooglePlaces
import json
import pickle

API_KEY = 'your_key'
google_places = GooglePlaces(API_KEY)

if __name__ == "__main__":
    food_types = [
        'african',
        'american',
        'asian',
        'chinese',
        'fast food',
        'french',
        'georgian',
        'german',
        'greek',
        'indian',
        'italian',
        'japanese',
        'korean',
        'latin american',
        'mexican',
        'pizza',
        'russian',
        'seafood',
        'spanish',
        'sushi',
        'thai',
        'turkish',
        'vietnamese'
    ]

    restaurants = dict()

    for cuisine in food_types:
        print(f'\n===== {cuisine} =====')
        query_result = google_places.text_search(
            query=cuisine + 'restaurant',
            location='Stuttgart, Germany',
            radius=20000)

        with open(f'query_result_{cuisine.replace(" ", "_")}.pickle', 'wb') as f:
            pickle.dump(query_result, f)

        # with open(f'query_result_{cuisine.replace(" ", "_")}.pickle', 'rb') as f:
        #     query_result = pickle.load(f)

        for place in query_result.places:
            place.get_details()
            details = place.details

            address_elements = ['route', 'locality', 'sublocality']
            address = {key: entry['long_name'] for entry in details['address_components']
                                for key in address_elements if key in entry['types']}

            # make sure it's in Stuttgart
            legit = ['Stuttgart',
                     'Esslingen am Neckar',
                     'Waiblingen',
                     'Sindelfingen',
                     'Leonberg',
                     'Böblingen',
                     'Kornwestheim'
                     ]
            if address['locality'] not in legit:
                print(f'Excluded restaurant in {address["locality"]}')
                break

            # clean up the name from address elements
            name = details['name']
            for word in address.values():
                if word in name:
                    print(f'Replaced "{word}" in: {name}')
                    name = name.replace(word, '').strip().strip('-').strip()
            details['name'] = name

            del details['geometry']

            if 'rating' in details:
                details['rating'] = str(details['rating'])

            details['cuisine'] = [cuisine]

            if name in restaurants:
                # same address -> add cuisine type
                # actually this was a bad idea, so probably remove it
                if address['route'] in restaurants[name]['formatted_address']:
                    if cuisine not in restaurants[name]['cuisine']:
                        restaurants[name]['cuisine'].append(cuisine)
                        print(f'Updated {name}, now says: {restaurants[name]["cuisine"]}')
                else:
                    print(f'Skipping {name} at a different location')
            else:
                restaurants[name] = details
                print(f'Added {name}')

    with open('../../more_restaurants.json', 'w') as f:
        json.dump(restaurants, f, indent=4)
