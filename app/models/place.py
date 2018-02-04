from app.utils import remove_duplicates


class Place:
    def __init__(self, storage):
        self.storage = storage
        self.index = 'headbang.foursquare.venues'
        self.type = 'venue'

    def get(self, size: int = 10):
        '''
        '''
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

        return list(map(lambda p: p['_source'], places))

    def post(self, places: dict):
        '''
        '''
        responses = []
        for place in places:
            response = self.storage.Elasticsearch.index(index=self.index, type=self.type,
                body=place, id=place['id'])
            responses.append(response)
        return responses

    def get_fbids(self, size: int = 10):
        '''
        '''
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

        return remove_duplicates(map(lambda p: p['_source']['contact']['facebookUsername'], places))

    def get_latlong(self, size: int = 10):
        '''
        '''
        places = self.storage.Elasticsearch.search(index=self.index, type=self.type,
            body={
            "size": size,
            "_source": [
                "location.labeledLatLngs.lat",
                "location.labeledLatLngs.lng"
            ],
            "query": {
                "bool": {
                    "must": [
                    {
                        "exists": {
                            "field": "location.labeledLatLngs.lat"
                        }
                    },
                    {
                        "exists": {
                            "field": "location.labeledLatLngs.lng"
                        }
                    }]
                }
            },
            "sort": [
            {
                "stats.checkinsCount": {
                    "order": "desc"
              }
            }]})['hits']['hits']

        return remove_duplicates(map(lambda p: '%s,%s' % (p['_source']['location']['labeledLatLngs'][0]['lat'], p['_source']['location']['labeledLatLngs'][0]['lng']), places))
