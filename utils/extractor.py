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


def extract_cuisine(details_dict):
    """
    Returns the cuisine of this restaurant. 
    """
    result = details_dict["cuisine"][0]
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
    "wheelchair_accessible_entrance": extract_wheelchair_accessible_entrance,
    "cuisine": extract_cuisine
}