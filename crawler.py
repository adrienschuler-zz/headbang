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
    def foursquare_venues(self, latlong=['48.8528417309667,2.36918060506559']):
        '''
        '''
        foursquare = Foursquare(Config.apis['foursquare'])

        current_latlong = request.get('%s/places/latlong/' % api_endpoint, params={'size': 200}).json()

        if current_latlong:
            latlong = current_latlong

        for ll in latlong:
            Log.info(ll)
            venues = foursquare.get_venues(ll)['venues']
            Log.info(venues)

            if venues:
                response = request.post('%s/places/' % api_endpoint, data=json.dumps(venues))
                Log.info(response.json())

    def facebook_events(self, fbids=[]):
        '''
        '''
        facebook = Facebook(Config.apis['facebook'])
        fbids = request.get('%s/places/fbids/' % api_endpoint, params={'size': 200}).json()

        for fbid in fbids:
            try:
                events = facebook.get_events(fbid)
                Log.info(events)

                if 'data' in events and events['data']:
                    response = request.post('%s/events/' % api_endpoint, data=json.dumps(events['data']))
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
