from utils.conf import load_conf

from crawlers.foursquare import Foursquare
from crawlers.facebook import Facebook


config = {}
config['apis'] = load_conf('apis')

foursquare = Foursquare(config['apis']['foursquare'])
facebook = Facebook(config['apis']['facebook'])

# print(foursquare.get_venues())
# print(facebook.get_events(180056048702133))
