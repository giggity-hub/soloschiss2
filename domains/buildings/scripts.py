from utils.google_places_api import google_places, query_result_to_detailed_list, detailed_list_to_table
import simplejson
import json
import os

this_dir = os.path.dirname(__file__)
scraped_path = os.path.join(this_dir, 'scraped.json')
table_path = os.path.join(this_dir, 'table.csv')

def scrape():
    query_result = google_places.nearby_search(
            location='Stuttgart, Germany', keyword='castle',
            radius=20000)

    scraping_result = query_result_to_detailed_list(query_result)
    print(scraping_result)

    with open(scraped_path, 'w+') as f:
        simplejson.dump(scraping_result, f, indent=4)

def write():
    with open(scraped_path) as f:
        details_list = simplejson.load(f)

    table = detailed_list_to_table(details_list)
    table.to_csv(table_path, index=False)


if __name__ == "__main__":
    # scrape()
    write()