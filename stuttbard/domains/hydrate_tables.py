def extract_house_number(details_dict):
    def filter_street_number(address_component):
        return "street_number" in address_component["types"]
    street_number_components = filter(filter_street_number, details_dict["address_components"])
    street_number = street_number_components[0]["short_name"]
    return street_number

def extract_phone_number(details_dict):
    pass

# The extractor dict contains all the extractor functions for the desired columns
# An extractor function receives a details dict for a specific name
# Define all the missing functions
# If you see any usefull attributes in the scraped data also add an extractor function for those
extractor = {
    "house_number": extract_house_number,
    "street": extract_street_name,
    "zip_code": extract_zip_code,
    "phone_number": extract_phone_number,
    "url": extract_url,
    ""
}


def add_col(table, scraped_data_dict, col_name):
    def get_extracted_value(row):
        name = row['name']
        details_dict = scraped_data_dict[name]
        col_val = extractor[col_name](details_dict)
        return col_val

    table[col_name] = table.apply(get_extracted_value, axis=1 )
    return table


# You can add a column to a table like this now
table = add_col(table, {}, 'house_number')
table = add_col(table, {}, 'phone_number')
