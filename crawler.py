#!/usr/bin/python

"""crawler.py -
Usage: crawler.py (--action <action>) [--api_endpoint <api_endpoint>]

Options:
    -h --help                      Show this message.
    --action=<action>              Crawler action.
    --api_endpoint=<api_endpoint>  Headbang API endpoint [default: http://localhost:5000].
"""

import json
import requests
from docopt import docopt
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

from app import logging, Config

from crawlers.foursquare import Foursquare
from crawlers.facebook import Facebook
from crawlers.google import Google

request = requests.Session()
retries = Retry(total=3, backoff_factor=1)
request.mount('http://', HTTPAdapter(max_retries=retries))


class Crawler:

    def __init__(self, **kwargs):
        [setattr(self, key[2:], value) for key, value in kwargs.items()]
        self.foursquare_client = Foursquare(Config.apis['foursquare'])
        self.facebook_client = Facebook(Config.apis['facebook'])
        self.google_client = Google(Config.apis['google'])

    def foursquare_venues(self, latlong: list = ['52.497553,13.451327']):
        logging.debug('foursquare_venues')
        response = request.get('%s/places/' % self.api_endpoint, params={'fields': ['lat', 'lng']}).json()
        logging.info(response)

        if response and 'error' not in response:
            latlong = response

        for ll in latlong:
            try:
                venues = self.foursquare_client.get_venues(ll)['venues']
                logging.info(venues)

                if venues:
                    response = request.post('%s/foursquare/venues/' % self.api_endpoint, data=json.dumps(venues)).json()
                    logging.info(response)

            except Exception as e:
                logging.error(e)

    def google_places(self):
        logging.debug('google_places')
        for venue in request.get('%s/foursquare/venues/' % self.api_endpoint).json():
            name = venue['_source']['name']
            latlong = venue['_source']['location']['labeledLatLngs'][0]
            google_place = self.google_client.get_places(name, latlong)

            if google_place['results'] and 'place_id' in google_place['results'][0]:
                details = self.google_client.get_place_details(google_place['results'][0]['place_id'])
                if details and 'result' in details:
                    logging.info(details['result'])
                    response = request.post('%s/google/places/' % self.api_endpoint, data=json.dumps(details['result'])).json()
                    logging.info(response)

    def facebook_places(self):
        logging.debug('facebook_places')
        for venue in request.get('%s/foursquare/venues/' % self.api_endpoint).json():
            name = venue['_source']['name']
            latlong = '%s,%s' % (venue['_source']['location']['lat'], venue['_source']['location']['lng'])
            fb_places = self.facebook_client.get_places(name, latlong)

            if 'data' in fb_places and fb_places['data']:
                fbid = fb_places['data'][0]['id']
                details = self.facebook_client.get_place_details(fbid)
                response = request.post('%s/facebook/places/' % self.api_endpoint, data=json.dumps(details)).json()
                logging.info(response)

    def facebook_events(self, fbids: list = ['FestsaalKreuzberg']):
        logging.debug('facebook_events')
        response = request.get('%s/places/' % self.api_endpoint, params={'fields': 'fb'}).json()

        if response and 'error' not in response:
            fbids = response

        for fbid in fbids:
            logging.info(fbid)
            try:
                events = self.facebook_client.get_events(fbid)
                logging.info(events)

                if 'data' in events and events['data']:
                    response = request.post('%s/events/' % self.api_endpoint, data=json.dumps(events['data'])).json()
                    logging.info(response)

            except Exception as e:
                logging.error(e)


if __name__ == '__main__':
    args = docopt(__doc__)
    getattr(Crawler(**args), args['--action'])()
