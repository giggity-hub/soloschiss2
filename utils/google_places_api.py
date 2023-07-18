from googleplaces import GooglePlaces, types, lang
from dotenv import load_dotenv
import os

load_dotenv()


API_KEY = os.getenv("GOOGLE_PLACES_API_KEY")


# import this to use the google places api
google_places = GooglePlaces(API_KEY)

if __name__ == "__main__":
    print(f"your Places API key is: {API_KEY}")