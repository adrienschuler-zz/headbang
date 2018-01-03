import json
import requests

from utils import load_conf

from crawlers.foursquare import Foursquare
from crawlers.facebook import Facebook


config = {}
config['apis'] = load_conf('apis')
config['storage'] = load_conf('storage')

foursquare = Foursquare(config['apis']['foursquare'])

ll = '48.8528417309667,2.36918060506559'

venues = foursquare.get_venues(ll)['venues']
# print(venues)

if venues:
    response = requests.post('http://localhost:5000/places', data=json.dumps(venues))
    print(response.json())

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
