import foursquare


class Foursquare:

    def __init__(self, config: dict) -> dict:
        self.client = foursquare.Foursquare(client_id=config['client_id'], client_secret=config['client_secret'])

    def get_venues(self, ll: str = '48.8566,2.3522') -> dict:
        params = {
            'radius': 1000,
            'intent': 'browse',
            'll': ll,
            'limit': 100,
            'categoryId': '4bf58dd8d48988d1e5931735,5032792091d4c4b30a586d5c'
        }

        return self.client.venues.search(params=params)
