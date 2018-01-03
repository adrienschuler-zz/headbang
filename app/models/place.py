from app import _storage


class Place():
    def __init__(self):
        self.es = {
            'index': 'foursquare.venues',
            'type': 'venue'
        }

    def show(self):
        _storage['es'].search(
            index=self.es['index'],
            type=self.es['type'],
            body={
                'query': {'match_all': {}}
            })

    def post(self, places: dict):
        for place in places:
            return _storage['es'].index(
                index=self.es['index'],
                type=self.es['type'],
                doc=place)
