import foursquare


class Foursquare:

    def __init__(self, config: dict):
        self.client = foursquare.Foursquare(client_id=config['client_id'], client_secret=config['client_secret'])

    def get_venues(self, ll: str = '48.8566,2.3522') -> dict:
        params = {
            'radius': 400,
            'intent': 'browse',
            'll': ll,
            'limit': 50,
            'categoryId': '4bf58dd8d48988d1e5931735,5032792091d4c4b30a586d5c'
        }

        search = ''
        for key in params.keys():
            search += '%s=%s&' % (key, params[key])
        print(search)

        return self.client.venues.search(params=params)
