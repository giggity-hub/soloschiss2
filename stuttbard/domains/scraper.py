import os
from googleplaces import GooglePlaces, types, lang
from stuttbard.domains.dataframes import load
import simplejson
import json

google_places = GooglePlaces('AIzaSyC5s1kNQiLrbe6_OwGZlSzEUOLzP1zLOJE')

def get_details_for_place_name(name):
    query_result = google_places.text_search(name, location="Stuttgart")
    print(query_result)
    place = query_result.places[0]
    print(place)
    place.get_details()
    
    return place.details

dir = "tables"


def extract_shit_and_save(df, out_file):
    print(df)
    names = df['name'].tolist()
    # print(names)
    res = {}
    for name in names:
        print(name)
        res[name] = get_details_for_place_name(name)

    with open(out_file, "w+", encoding="utf8") as f:
        simplejson.dump(res, f)

def main():
    current_dir = os.path.dirname(__file__)
    
    domains = load()
    
    for domain in domains.keys():
        out_file = os.path.join(current_dir, "scraping_results", f"{domain}.json")
        df = domains[domain]
        extract_shit_and_save(df, out_file)


if __name__ == "__main__":
    main()
    # x = get_details_for_place_name("Staatsgallerie")
    # print(x)
    # domains = load()
    # # print(domains)
    # print(domains['museum']['name'].tolist())