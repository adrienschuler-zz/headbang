from facebook import GraphAPIError

from utils.conf import load_conf

from crawlers.foursquare import Foursquare
from crawlers.facebook import Facebook

from storage.elasticsearch import ES

from indexers.elasticsearch import *


config = {}
config['apis'] = load_conf('apis')
config['storage'] = load_conf('storage')

es = ES(config['storage']['elasticsearch'])

# foursquare = Foursquare(config['apis']['foursquare'])
# Venue = FoursquareVenue(es)

# for ll in lls:
#     venues = foursquare.get_venues(ll)['venues']
#     if venues:
#         response = Venue.bulk(venues)
#         print(response)


# facebook = Facebook(config['apis']['facebook'])
# Event = FacebookEvent(es)
# for fbid in fbids:
#     try:
#         events = facebook.get_events(fbid)['data']
#         print(events)
#         if events:
#             print(Event.bulk(events))
#     except GraphAPIError:
#         pass
