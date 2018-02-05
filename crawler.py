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

api_endpoint = 'http://localhost:5000'


class Crawler:

    def __init__(self):
        self.foursquare_client = Foursquare(Config.apis['foursquare'])
        self.facebook_client = Facebook(Config.apis['facebook'])

    def foursquare_venues(self, latlong: list = ['48.852841,2.369180', '48.882603,2.340201', '48.893904,2.393163']):
        '''
        '''
        response = request.get('%s/places/' % api_endpoint, params={'fields': ['lat', 'lng']}).json()
        Log.info(response)

        if response and 'error' not in response:
            latlong = response

        for ll in latlong:
            try:
                venues = self.foursquare_client.get_venues(ll)['venues']
                Log.info(venues)

                if venues:
                    response = request.post('%s/places/' % api_endpoint, data=json.dumps(venues)).json()
                    Log.info(response)

            except Exception as e:
                Log.error(e)

    def facebook_events(self, fbids: list = ['ZenithParisLaVillette', 'LaCigaleParis', 'supersonicbastille']):
        '''
        '''
        response = request.get('%s/places/' % api_endpoint, params={'fields': 'fb'}).json()
        Log.info(response)

        if response and 'error' not in response:
            fbids = response

        for fbid in fbids:
            try:
                events = self.facebook_client.get_events(fbid)
                Log.info(events)

                if 'data' in events and events['data']:
                    response = request.post('%s/events/' % api_endpoint, data=json.dumps(events['data'])).json()
                    Log.info(response)

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
