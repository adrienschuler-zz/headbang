from app.utils import remove_duplicates


class Place:
    def __init__(self, storage):
        self.storage = storage

        self.index = 'headbang.places'
        self.type = 'place'

        self.sources = {
            'google': {
                'index': 'headbang.google.places',
                'type': 'place'
            },
            'facebook': {
                'index': 'headbang.facebook.places',
                'type': 'place'
            },
            'foursquare': {
                'index': 'headbang.foursquare.venues',
                'type': 'venue'
            }
        }

    def get(self, size: int = 100, fields: str = '') -> list:
        '''
        '''
        query = {
            "size": size,
            "query": {
                "match_all": {}
            }
        }

        if fields:
            source = ['id']
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
            response = self.storage.Elasticsearch.index(
                index=self.index,
                type=self.type,
                body=place,
                id=place['id']
            )
            responses.append(response)
        return responses

    def get_source(self, source, size: int = 100) -> list:
        '''
        '''
        return self.storage.Elasticsearch.search(
            index=self.sources[source]['index'],
            type=self.sources[source]['type'],
            body={
                "size": size,
                "query": {"match_all": {}}
            }
        )['hits']['hits']

    def post_source(self, source, places) -> list:
        '''
        '''
        responses = []
        if type(places) is list:
            for place in places:
                response = self.storage.Elasticsearch.index(
                    index=self.sources[source]['index'],
                    type=self.sources[source]['type'],
                    body=place,
                    id=place['id']
                )
                responses.append(response)
        elif type(places) is dict:
            response = self.storage.Elasticsearch.index(
                index=self.sources[source]['index'],
                type=self.sources[source]['type'],
                body=places,
                id=places['id']
            )
            responses.append(response)

        return responses
