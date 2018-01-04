from app import Storage


class Place:
    def __init__(self):
        self.es = {
            'index': 'foursquare.venues',
            'type': 'venue'
        }

    def show(self):
        return Storage.Elasticsearch.search(
            index=self.es['index'],
            type=self.es['type'],
            body={
                'query': {'match_all': {}}})

    def post(self, places: dict):
        for place in places:
            return Storage.Elasticsearch.index(
                index=self.es['index'],
                type=self.es['type'],
                doc=place)
