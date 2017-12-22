import json


class FoursquareVenue(ESIndexer):
    def __init__(self, ESInstance):
        super().__init__(ESInstance)
        self.index = 'foursquare.venues'
        self.type = 'venue'
        self.id_field = ['id']


class FacebookEvent(ESIndexer):
    def __init__(self, ESInstance):
        super().__init__(ESInstance)
        self.index = 'facebook.events'
        self.type = 'event'
        self.id_field = ['id']
