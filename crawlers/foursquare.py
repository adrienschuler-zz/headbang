import foursquare


class Foursquare:

    def __init__(self, config: dict) -> dict:
        self.client = foursquare.Foursquare(client_id=config['client_id'], client_secret=config['client_secret'])

        # https://developer.foursquare.com/docs/resources/categories
        self.categories = [
            '4bf58dd8d48988d116941735',  # Bar
            '56aa371ce4b08b9a8d57356c',  # Beer Bar
            '4bf58dd8d48988d1e5931735',  # Beer Garden

            '4bf58dd8d48988d1e5931735',  # Music Venue
            '4bf58dd8d48988d1e9931735',  # Rock Club

            '5267e4d9e4b0ec79466e48d1',  # Music Festival

            '5032792091d4c4b30a586d5c',  # Concert Hall
        ]

    def get_venue(self, venue_id: str) -> dict:
        return self.client.venues(venue_id)

    def search_venues(self, latlong: str) -> dict:
        params = {
            'radius': 2000,
            'intent': 'browse',
            'll': latlong,
            'limit': 200,
            'categoryId': ','.join(self.categories)
        }

        return self.client.venues.search(params=params)
