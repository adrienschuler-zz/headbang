class Place:
    def __init__(self, storage):
        self.storage = storage
        self.index = 'foursquare.venues'
        self.type = 'venue'

    def get(self, size: int = 10):
        places = self.storage.Elasticsearch.search(index=self.index, type=self.type,
            body={
            "size": size,
            "query": {
                "match_all": {}
            },
            "sort": [{
                "stats.checkinsCount": {
                    "order": "desc"
                }
            }]
        })['hits']['hits']

        return list(map(lambda place: place['_source'], places))

    def get_facebook_ids(self, size: int = 10):
        places = self.storage.Elasticsearch.search(index=self.index, type=self.type,
            body={
            "size": size,
            "_source": "contact.facebookUsername",
            "query": {
                "exists": {
                    "field": "contact.facebookUsername"
                }
            },
            "sort": [{
                "stats.checkinsCount": {
                    "order": "desc"
                }
            }]
        })['hits']['hits']

        return list(map(lambda place: place['_source']['contact']['facebookUsername'], places))

    def post(self, places: dict):
        responses = []
        for place in places:
            response = self.storage.Elasticsearch.index(index=self.index, type=self.type,
                body=place, id=place['id'])
            responses.append(response)
        return responses
