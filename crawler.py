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
from crawlers.google import Google

request = requests.Session()
retries = Retry(total=3, backoff_factor=1)
request.mount('http://', HTTPAdapter(max_retries=retries))

api_endpoint = 'http://localhost:5000'


class Crawler:

    def __init__(self):
        self.foursquare_client = Foursquare(Config.apis['foursquare'])
        self.facebook_client = Facebook(Config.apis['facebook'])
        self.google_client = Google(Config.apis['google'])

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
                    response = request.post('%s/foursquare/venues/' % api_endpoint, data=json.dumps(venues)).json()
                    Log.info(response)

            except Exception as e:
                Log.error(e)

    def google_places(self):
        '''
        '''
        for venue in request.get('%s/foursquare/venues/' % api_endpoint).json():
            name = venue['_source']['name']
            latlong = venue['_source']['location']['labeledLatLngs'][0]
            google_place = self.google_client.get_places(name, latlong)

            if google_place['results'] and 'place_id' in google_place['results'][0]:
                details = self.google_client.get_place_details(google_place['results'][0]['place_id'])
                if details and 'result' in details:
                    Log.info(details['result'])
                    response = request.post('%s/google/places/' % api_endpoint, data=json.dumps(details['result'])).json()
                    Log.info(response)

    def facebook_places(self):
        '''
        '''
        for venue in request.get('%s/foursquare/venues/' % api_endpoint).json():
            name = venue['_source']['name']
            latlong = '%s,%s' % (venue['_source']['location']['lat'], venue['_source']['location']['lng'])
            fb_places = self.facebook_client.get_places(name, latlong)

            if 'data' in fb_places:
                fbid = fb_places['data'][0]['id']
                details = self.facebook_client.get_place_details(fbid)
                response = request.post('%s/facebook/places/' % api_endpoint, data=json.dumps(details)).json()
                Log.info(response)

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

parser.add_argument('--google_places',
    help='Crawl Google places',
    action='store_true')

parser.add_argument('--facebook_places',
    help='Crawl Facebook places',
    action='store_true')

parser.add_argument('--facebook_events',
    help='Crawl Facebook Events for provided list of facebook page ids',
    action='store_true')

crawler = Crawler()
args = parser.parse_args()

if args.foursquare_venues:
    crawler.foursquare_venues()

if args.google_places:
    crawler.google_places()

if args.facebook_places:
    crawler.facebook_places()

if args.facebook_events:
    crawler.facebook_events()
