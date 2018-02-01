#
# Usage: python crawler.py -h
#

import json
import argparse
import requests
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

from app import Log, Config

from crawlers.foursquare import Foursquare
from crawlers.facebook import Facebook

request = requests.Session()
retries = Retry(total=3, backoff_factor=1)
request.mount('http://', HTTPAdapter(max_retries=retries))


class Crawler:
    def foursquare_venues(self, ll=[]):
        foursquare = Foursquare(Config.apis['foursquare'])
        ll = '48.8528417309667,2.36918060506559'
        venues = foursquare.get_venues(ll)['venues']
        Log.info(venues)

        if venues:
            response = request.post('http://localhost:5000/places', data=json.dumps(venues))
            Log.info(response.json())

    def facebook_events(self, fbids=[]):
        facebook = Facebook(Config.apis['facebook'])
        fbids = ['hardrockcafeparis', 'ZenithParisLaVillette', 'gaitelyrique', 'PointEphemere', 'olympiabrunocoquatrix', 'lebataclan', 'LaCigaleParis', 'LeCasinodeParis', 'paris', 'international.oberkampf', 'HarrysNewYorkBarParis', 'trabendo.paris', 'lagrossecaisseparis', 'paris', 'petitbain', 'truskelmicroclub', 'LesFoliesBergerePageOfficielle', 'flowparis', 'lalimentation.generale', 'elyseemontmartreofficiel', 'paris', 'lajavabelleville', 'AlhambraTheatreParis', 'damedecanton', '59rivoli', 'gibusclub', 'LaBouleNoire', 'ducdeslombards', 'lamecaniqueondulatoire', 'sallegaveau', 'TheatreduPalaisRoyal', 'AperockCafe', 'CharlotteBarBastille', 'theatre.de.menilmontant', 'Studio.de.lErmitage', 'supersonicbastille', 'paris', 'letageparis', 'EtoilesParis', 'RelaisDeLaHuchette', 'cafelaurent75', 'TheStation75', 'UarenaOfficiel', 'lamaisonsage', 'maisondelaradio', 'stationgaredesmines', 'buzzjaamsono', 'clubrayeparis', 'paris', 'maisondelaradio', 'LaGareJazz', 'maisondelaradio', 'CandyShopParis', 'maisondelaradio', 'wonder.st.ouen']

        Log.info(fbids)

        for fbid in fbids:
            try:
                events = facebook.get_events(fbid)
                Log.info(events)

                if events['data']:
                    response = request.post('http://localhost:5000/events', data=json.dumps(events))
                    Log.info(response.json())

            except Exception as e:
                Log.error(e)


parser = argparse.ArgumentParser(description='')

parser.add_argument('--foursquare_venues',
    help='Crawl Foursquare venues around provided list of latitude,longitude',
    action='store_true')

parser.add_argument('--facebook_events',
    help='Crawl Facebook Events for provided list of facebook page ids',
    action='store_true')

crawler = Crawler()
args = parser.parse_args()

if args.foursquare_venues:
    crawler.foursquare_venues()

if args.facebook_events:
    crawler.facebook_events()
