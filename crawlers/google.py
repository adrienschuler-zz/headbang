import googlemaps


class Google:

    def __init__(self, config: dict) -> dict:
        self.client = googlemaps.Client(key=config['api_key'])

    def get_places(self, query: str = '', ll: dict = {'lat': 48.85026572254583, 'lng': 2.3697217372873}) -> dict:
        return self.client.places(
            query,
            location=ll,
            radius=100
        )

    def get_place_details(self, place_id):
        return self.client.place(place_id)
