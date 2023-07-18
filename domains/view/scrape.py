from utils.google_places_api import google_places

keywords = ['Aussichtsplatform', 'Aussichtspunkt', 'Aussichtsturm']

query_result = google_places.nearby_search(
        location='London, England', keyword='Fish and Chips',
        radius=20000, types=[types.TYPE_FOOD])