from googleplaces import GooglePlaces, types, lang
from dotenv import load_dotenv
from utils.extractor import extractor
import os
import pandas as pd

load_dotenv()
API_KEY = os.getenv("GOOGLE_PLACES_API_KEY")


google_places = GooglePlaces(API_KEY)

def query_result_to_detailed_list(query_result):
    res = []
    for place in query_result.places:
        place.get_details()
        res.append(place.details)
    return res

def details_dict_to_row(details_dict):
    row = {}
    for key, fn in extractor.items():
        try:
            row[key] = fn(details_dict)
        except:
            row[key] = None
    return row

def detailed_list_to_table(detailed_list):
    rows = map(details_dict_to_row, detailed_list)
    table = pd.DataFrame(rows)
    return table


def get_details_for_place_name(name):
    query_result = google_places.text_search(name, location="Stuttgart")
    place = query_result.places[0]
    place.get_details()
    return place.details

def names_to_detailed_list(names):
    details = map(get_details_for_place_name, names)
    return list(details)


if __name__ == "__main__":
    print(f"your Places API key is: {API_KEY}")