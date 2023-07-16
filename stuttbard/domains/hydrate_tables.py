"""
    This script is used to fill csv tables or edit csv tables, based on the json file obatained 
    from google places api.

    In order to add another attribute (i.e. column) to your csv table, you have to define an 
    extract function that extracts the values for the column. 
    Additional, you have to add an entry of the form "<colum_name>: <extract_function_name>" to
    the extractor dict.

    Note: You are not allowed to add an entry of the form "name: <extract_function_name>", because
    there is already a column called "name" reserved. This "name" column holds the keys to look up
    specific entries in the json file.
"""

import json
import pandas as pd
import os

def extract_city(details_dict):
    """
    Returns the city of the location specified in details_dict.
    """
    def filter_city(address_component):
        return "locality" in address_component["types"]
    city_componenets = list(filter(filter_city, details_dict["address_components"]))
    city = city_componenets[0]["long_name"]
    return city


def extract_area(details_dict):
    """
    Returns the area of the location specified in details_dict like (e.g. middle, south, north, east, west ...).
    """
    def filter_area(address_component):
        return "sublocality_level_1" in address_component["types"]
    area_componenets = list(filter(filter_area, details_dict["address_components"]))
    area = area_componenets[0]["short_name"]
    return area


def extract_house_number(details_dict):
    """
    Returns the house number of the location specified in details_dict.
    """
    def filter_street_number(address_component):
        return "street_number" in address_component["types"]
    street_number_components = list(filter(filter_street_number, details_dict["address_components"]))
    street_number = street_number_components[0]["short_name"]
    return street_number


def extract_street(details_dict):
    """
    Returns the street name of the location specified in details_dict.
    """
    def filter_street(address_component):
        return "route" in address_component["types"]
    street_components = list(filter(filter_street, details_dict["address_components"]))
    street = street_components[0]["short_name"]
    return street


def extract_postal_code(details_dict):
    """
    Returns the postal code of the location specified in details_dict.
    """
    def filter_postal_code(address_component):
        return "postal_code" in address_component["types"]
    postal_code_components = list(filter(filter_postal_code, details_dict["address_components"]))
    postal_code = postal_code_components[0]["short_name"]
    return postal_code


def extract_location_lat(details_dict):
    """
    Returns the latitude of the location specified in details_dict.
    """
    result = details_dict["geometry"]["location"]["lat"]
    return result


def extract_location_lng(details_dict):
    """
    Returns the longitude of the location specified in details_dict.
    """
    result = details_dict["geometry"]["location"]["lng"]
    return result


def extract_phone_number(details_dict):
    """
    Returns the phone number of the location specified in details_dict.
    """
    # this is the local phone number in the format "07XX XXXXXXXX"
    # result = details_dict["formatted_phone_number"]

    # this is the international phone number in the format "+49 XXX XXXXXXXX"
    result = details_dict["international_phone_number"]
    return result


def extract_long_name(details_dict):
    """
    Returns the human-readable name for the place specified in details_dict. 
    """
    result = details_dict["name"]
    return result


def extract_place_id(details_dict):
    """
    Returns a textual identifier that uniquely identifies a place. To retrieve information about the place, 
    pass this identifier in the place_id field of a Places API request.
    """
    result = details_dict["place_id"]
    return result


def extract_plus_code(details_dict):
    """
    Returns the globally valid google plus code of the location specified in details_dict.
    The plus code is derived from latitude and longitude coordinates, that represents an area: 
    1/8000th of a degree by 1/8000th of a degree (about 14m x 14m at the equator) or smaller.
    """
    result = details_dict["plus_code"]["global_code"]
    return result


def extract_rating(details_dict):
    """
    Returns the place's rating, from 1.0 to 5.0, based on aggregated user reviews. 
    """
    result = details_dict["rating"]
    return result


def extract_price_level(details_dict):
    """
    The price level of the place, on a scale of 0 to 4. 
    The exact amount indicated by a specific value will vary from region to region. 
    Price levels are interpreted as follows:
    0 Free
    1 Inexpensive
    2 Moderate
    3 Expensive
    4 Very Expensive 
    """
    result = details_dict["price_level"]
    return result


def extract_url(details_dict):
    """ 
    Returns the URL of the official Google page for this place.
    """
    result = details_dict["url"]
    return result


def extract_vicinity(details_dict):
    """
    Returns a simplified address for the location including the street name, 
    street number, and locality, but not the province/state, postal code, or country. 
    """
    result = details_dict["vicinity"]
    return result


def extract_website(details_dict):
    """
    The authoritative website for this place, such as a business' homepage. 
    """
    result = details_dict["website"]
    return result


def extract_wheelchair_accessible_entrance(details_dict):
    """
    Specifies if the place has an entrance that is wheelchair-accessible. 
    """
    result = details_dict["wheelchair_accessible_entrance"]
    return result


# The extractor dict contains all the extractor functions for the desired columns
# An extractor function receives a details dict for a specific name
# Define all the missing functions
# If you see any usefull attributes in the scraped data also add an extractor function for those
extractor = {
    "house_number": extract_house_number,
    "street": extract_street,
    "area": extract_area,
    "postal_code": extract_postal_code,
    "city": extract_city,
    "location_lat": extract_location_lat,
    "location_lng": extract_location_lng,

    "long_name": extract_long_name,
    "phone_number": extract_phone_number,
    "website": extract_website,
    "url": extract_url,
    "plus_code": extract_plus_code,
    "place_id": extract_place_id,
    "rating": extract_rating,
    "price_level": extract_price_level,
    "vicinity": extract_vicinity,
    "wheelchair_accessible_entrance": extract_wheelchair_accessible_entrance
}


def add_col(table, scraped_data_dict, col_name):
    """
    Adds a single column to the table based on data extracted from scraped_data_dict.
    The attribute to fill in the new column is specified by the col_name.
    
    Note: Can not be used on an empty table. The table must at least contain a "name" column with
    the name values corresponding to the keys of the scraped_data_dict.

    Parameters
    ----------
    table : pandas DataFrame
        The DataFrame obtained by reading a csv file with pandas.
    scraped_data_dict : dict
        The dict obtained by reading a json file obtained from google places api.
    col_name : string
        The string that specifies the attribute to extract from the json data.
    
    Returns
    ----------
    table : pandas DataFrame
        The DataFrame with a new column filled with data from scraped_data_dict.
    """
    def get_extracted_value(row):
        name = row['name']
        details_dict = scraped_data_dict[name]
        try:
            # in case a certain attribute can not be extracted from a details_dict we will fill "None"
            col_val = extractor[col_name](details_dict)
        except:
            col_val = "None"
        return col_val
    
    table[col_name] = table.apply(get_extracted_value, axis=1 )
    return table


def remove_columns(table, col_names=[]):
    """
    Removes the columns specified by col_names from the table.

    Parameters
    ----------
    table : pandas DataFrame
        The DataFrame obtained by reading a csv file with pandas.
    col_name : list of strings
        The list of strings holds column names of those columns that should be deleted from the table. 

    Returns
    ----------
    table : pandas DataFrame
        The DataFrame with the deleted columns.
    """
    if len(col_names) != 0:
        table = table.drop(col_names, axis=1)
    return table


def get_table(scraped_data_dict, columns=[]):
    """
    Creates a pandas DataFrame based on the values obtained from the scraped_data_dict dict.
    This function should do the same as the extract_table(...) function, but the order of the rows
    in the tables can be different.
    
    Note: The "name" column holds the key values for the scraped_data_dict. The "long_name"
    column holds the detailed names for the places.

    Parameters
    ----------
    scraped_data_dict : dict
        The dict obtained by reading a json file obtained from google places api.

    columns : list of strings
        The name of the colums we want to extract from the scraped_data_dict. 
        These should correspond to a subset of keys from extarctor dict.
        If columns is a empty list all possible columns defined by the above extractor dict,
        will be extracted.
    
    Returns
    ----------
    table : pandas DataFrame
        The DataFrame filled with values from the scraped_data_dict.
    """
    lookup_names = list(scraped_data_dict.keys())
    data_dict = {}

    if len(columns) == 0:
        columns = list(extractor.keys())
    assert(not "name" in columns)

    for col_name in columns:
        column = []
        for lookup_name in lookup_names:
            details_dict = scraped_data_dict[lookup_name]
            try:
                column.append(extractor[col_name](details_dict))
            except:
                column.append("None")
        data_dict[col_name] = column
    
    # the lookup_names column in the dataframe can be later used to lookup the json file scraped_data_dict
    # in order to obtain specific details_dict
    data_dict["name"] = lookup_names

    dataframe = pd.DataFrame.from_dict(data_dict)
    # TODO: add some sorting of the dataframe according to the values of one column.
    # This ensures we always get the same table back and don't have the rows in abitrary order everytime
    # we call this function.

    return dataframe


def extend_table(table, scraped_data_dict, columns=[]):
    """
    Takes a table as input and extends with columns filled by data from the scrapped_data_dict.
    The columns that should be extracted from scrapped_data_dict and added to the table
    are specified by the columns list. If columns is empty all available data in the 
    scrapped_data_dict is added.

    Note: The table requires a column called "name" filled with the keys for the scrapped_data_dict.

    Parameters
    ----------
    table : pandas DataFrame
        The original DataFrame that should be extended by this method.

    scraped_data_dict : dict
        The dict obtained by reading a json file obtained from google places api.

    columns : list of strings
        The name of the colums we want to extract from the scraped_data_dict. 
        These should correspond to a subset of keys from extarctor dict.
        If columns is a empty list all possible columns defined by the above extractor dict,
        will be extracted.
    
    Returns
    ----------
    extended_table : pandas DataFrame
        The DataFrame extended by new columns with values from the scraped_data_dict.
    """
    if len(columns) == 0:
        columns = list(extractor.keys())
    assert(not "name" in columns)

    for column_name in columns:
        # the add_col(...) function requires the table to have the "name" column
        table = add_col(table, scraped_data_dict, column_name)

    return table


def extract_table(scraped_data_dict, columns=[]):
    """
    Creates a pandas DataFrame based on the values obtained from the scraped_data_dict dict.
    
    Note: Does the same thing as the get_table(...) function, but relies on the add_col(...) function.
    Therefore if add_col works this function will probably also work. However, the order of rows can 
    be different. 

    Note: The returned table has a column called "name" filled with the keys for the scrapped_data_dict.
    These are different from the values in the column called "long_name" that holds the detailed name of
    a place.

    Parameters
    ----------
    scraped_data_dict : dict
        The dict obtained by reading a json file obtained from google places api.

    columns : list of strings
        The name of the colums we want to extract from the scraped_data_dict. 
        These should correspond to a subset of keys from extarctor dict.
        If columns is a empty list all possible columns defined by the above extractor dict,
        will be extracted.
    
    Returns
    ----------
    table : pandas DataFrame
        The DataFrame filled with values from the scraped_data_dict.
    """
    # Creates a table with one column called "names". The names are the keys to entries in the json dict.
    # This is required for the add_col function.
    table = pd.DataFrame({"name": list(scraped_data_dict.keys())})
    extend_table(table, scraped_data_dict, columns=[])
    
    # TODO: add some sorting of the table so we get everytime the same table when this function is called.    
    return table


def update_columns(old_table, scraped_data_dict, col_names=[]):
    """
    Updates the values from the columns specified by col_names in the table with the new data coming
    from scraped_data_dict. If one of the column names given in col_names is not a column in the
    table already, the column can also not be updated and thus will be ignored. 

    Parameters
    ----------
    table : pandas DataFrame
        The DataFrame obtained by reading a csv file with pandas.
    scraped_data_dict : dict
        The dict obtained by reading a json file obtained from google places api.
    col_name : list of strings
        The list of strings specifies columns to update with new values from scraped_data_dict. 

    Returns
    ----------
    table : pandas DataFrame
        The DataFrame with updated values in the specified columns.
    """
    new_dataframe = get_table(scraped_data_dict)
    # TODO: add code here
    pass


def test_table_extraction(path):
    """
    Can be used to test if the table extraction from a google places api json file to a pandas DataFrame works.
    
    Parameters
    ----------
    path : string
        The string defines the path to a json file obtained by the google places api.

    """
    jdata = read_json_file(path)
    
    table_a = extract_table(scraped_data_dict=jdata)
    table_b = get_table(scraped_data_dict=jdata)
    # check_like will make it ignore the order the rows and colums in the dataframe
    pd.testing.assert_frame_equal(table_a, table_b, check_like=True)

    # try here different subsets of keys from the extractor dict (see above in code) as columns
    table_a = extract_table(scraped_data_dict=jdata, columns=["city"])
    table_b = get_table(scraped_data_dict=jdata, columns=["city"])
    pd.testing.assert_frame_equal(table_a, table_b, check_like=True)

    return True


def test_json_structure(json_dict):
    assert("name" in json_dict.keys())
    assert("address_components" in json_dict.keys())
    assert("formatted_address" in json_dict.keys())
    assert("place_id" in json_dict.keys())
    assert("plus_code" in json_dict.keys())
    assert("global_code" in json_dict["plus_code"])
    assert("vicinity" in json_dict.keys())

    assert("international_phone_number" in json_dict.keys())
    assert("url" in json_dict.keys())
    assert("website" in json_dict.keys())
    assert("rating" in json_dict.keys())
    assert("wheelchair_accessible_entrance" in json_dict.keys())

    # TODO: finish the tests for the json structure


def read_json_file(path):
    """
    Reads a json file and returns a dict with the entries.
    """
    # Opening JSON file
    f = open(path)
    
    # returns JSON object as a dictionary
    data = json.load(f)

    # Closing file
    f.close()
    return data



def print_json_entry(details_dict):
    """
    Prints all information from a single entity of the json file based on the defined extractor methods.
    The json file is a dict that has the "name" of certain locations as a key and details_dict 
    as corresponding value.

    Parameters
    ----------
    details_dict : dict
        The dict obtained by specifying a "name" as key to the data dict obtained from readina a json file.
    """
    city = extract_city(details_dict)
    area = extract_area(details_dict)
    postal_code = extract_postal_code(details_dict)
    street = extract_street(details_dict)
    house_number = extract_house_number(details_dict)
    location_lat = extract_location_lat(details_dict)
    location_lng = extract_location_lng(details_dict)
    phone_number = extract_phone_number(details_dict)
    name = extract_long_name(details_dict)

    place_id = extract_place_id(details_dict)
    plus_code = extract_plus_code(details_dict)
    rating = extract_rating(details_dict)
    price_level = extract_price_level(details_dict)
    url = extract_url(details_dict)
    vicinity = extract_vicinity(details_dict)
    website = extract_website(details_dict)
    wheelchair_accessible_entrance = extract_wheelchair_accessible_entrance(details_dict)

    print("city:", city)
    print("area:", area)
    print("postal_code:", postal_code)
    print("street:", street)
    print("house_number:", house_number)
    print("location_lat:", location_lat)
    print("location_lng:", location_lng)

    print("phone_number:", phone_number)
    print("long_name:", name)

    print("place_id:", place_id)
    print("plus_code:", plus_code)
    print("rating:", rating)
    print("price_level:", price_level)
    print("url:", url)
    print("vicinity:", vicinity)
    print("website:", website)
    print("wheelchair_accessible_entrance:", wheelchair_accessible_entrance)


def main():
    # this way you get the dir name of the file regardless from where it is called
    current_dir = os.path.dirname(__file__)
    # directory filled with the json files obtained from google places api
    scraping_results_dir = os.path.join(current_dir, "scraping_results")
    scraping_files = [file for file in os.listdir(scraping_results_dir)]
    # directory of already existing csv tables that should be extended by json data from scraping_results 
    # directory
    tables_dir = os.path.join(current_dir, "tables")

    for scraping_file in scraping_files:
        try:
            json_dict = read_json_file(os.path.join(scraping_results_dir, scraping_file))
            old_csv_file_path = os.path.join(tables_dir, scraping_file.replace("json", "csv"))
            if os.path.isfile(old_csv_file_path):
                # if there is already a csv table we want to extend it by the data of the corresponding 
                # json file
                table = pd.read_csv(old_csv_file_path, delimiter=";") 
                #TODO: adapt the columns to the specific domain.
                table = extend_table(table, json_dict, columns=[])
            else:
                # if there is no csv table corresponding to the json file, we create a new one, 
                # based on the json data
                #TODO: adapt the columns to the specific domain.
                table = extract_table(scraped_data_dict=json_dict, columns=[])

            results_dir = os.path.join(current_dir, "extracted_tables")
            csv_file_path = os.path.join(results_dir, scraping_file.replace("json", "csv"))
            table.to_csv(csv_file_path, sep=";", index=False)
       
        except Exception as error:
            print(error)
            continue

if __name__ == "__main__":
    main()