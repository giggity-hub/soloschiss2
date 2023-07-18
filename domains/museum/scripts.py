from utils.google_places_api import google_places, query_result_to_detailed_list, detailed_list_to_table, names_to_detailed_list
import simplejson
import json
import os
import pandas as pd

this_dir = os.path.dirname(__file__)
scraped_path = os.path.join(this_dir, 'scraped.json')
base_table_path = os.path.join(this_dir, 'base.csv')
table_path = os.path.join(this_dir, 'table.csv')

def scrape():
    base_table = pd.read_csv(base_table_path)
    names = base_table['name'].tolist()

    scraping_result = names_to_detailed_list(names)
    print(scraping_result)

    with open(scraped_path, 'w+') as f:
        simplejson.dump(scraping_result, f, indent=4)

def write():
    with open(scraped_path) as f:
        details_list = simplejson.load(f)

    base_table = pd.read_csv(base_table_path)
    scraped_table = detailed_list_to_table(details_list)

    # Since the scraped data is in the same order as the base table we can just join them on the index column
    table = pd.concat([base_table, scraped_table], axis=1)
    table.to_csv(table_path, index=False)


if __name__ == "__main__":
    # scrape()
    write()