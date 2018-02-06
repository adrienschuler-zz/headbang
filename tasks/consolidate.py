from app import Storage, Config, Model, Log


class Consolidate:

    def __init__(self):
        pass

    def places(self):
        ''' Consolidate Foursquare venues
        '''
        places = []

        foursquare_venues = Storage.Elasticsearch.search(
            index='headbang.foursquare.places',
            type='places',
            body={
                "size": 200,
                "source": [
                    "_id",
                    "name",
                    "url",
                    "verified",
                    "categories",
                    "stats",
                    "contact.facebookUsername",
                    "location.formattedAddress",
                    "location.lat",
                    "location.lng"
                ],
                "query":{"match_all": {}}
            })

        for venue in foursquare_venues:
            pass
