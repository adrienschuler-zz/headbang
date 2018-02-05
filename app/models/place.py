from app.utils import remove_duplicates


class Place:
    def __init__(self, storage):
        self.storage = storage
        self.index = 'headbang.foursquare.venues'
        self.type = 'venue'

    def get(self, size: int = 100, fields: str = '') -> list:
        '''
        '''
        query = {
            "size": size,
            "query": {
                "match_all": {}
            },
            "sort": [{
                "stats.checkinsCount": {
                    "order": "desc"
                }
            }]
        }

        # TODO: remove this ugly things with index consolidation task
        mapping = {
            'lat': 'location.labeledLatLngs.lat',
            'lng': 'location.labeledLatLngs.lng',
            'fb': 'contact.facebookUsername'
        }

        if fields:
            source = []
            for field in fields:
                source.append(mapping[field])
            query['_source'] = source

        places = self.storage.Elasticsearch.search(index=self.index, type=self.type, body=query)['hits']['hits']

        return list(map(lambda p: p['_source'], places))

    def post(self, places: dict) -> list:
        '''
        '''
        responses = []
        for place in places:
            response = self.storage.Elasticsearch.index(index=self.index, type=self.type,
                body=place, id=place['id'])
            responses.append(response)
        return responses
