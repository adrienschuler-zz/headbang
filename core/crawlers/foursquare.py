import json
import foursquare


class Foursquare:

    def __init__(self, config):
        self.client = foursquare.Foursquare(client_id=config['client_id'], client_secret=config['client_secret'])

    def get_venues(self):
        params = {
            'intent': 'browse',
            'll': '48.85361,2.37455',
            'radius': 15000,
            'limit': 50,
            'categoryId': '4bf58dd8d48988d1e5931735,5032792091d4c4b30a586d5c'
        }

        return json.dumps(self.client.venues.search(params=params))
