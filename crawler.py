#!/usr/bin/python

"""crawler.py -
Usage: crawler.py (--action <action>) [--seeds <seeds>]... [--api_endpoint <api_endpoint>]

Options:
    -h --help                      Show this message.
    --action=<action>              Crawler action.
    --seeds=<seeds>...               Latitude,Longitude seeds [default 52.497553,13.451327].
    --api_endpoint=<api_endpoint>  Headbang API endpoint [default: http://localhost:5000].
"""

import json
import requests
import time
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
        self.api_clients = {
            'foursquare': Foursquare(Config.apis['foursquare']),
            'facebook': Facebook(Config.apis['facebook']),
            'google': Google(Config.apis['google'])
        }

    def headbang(self, verb, endpoint, datas: dict = {}, params: dict = {}):
        if verb == 'post':
            return request.post('%s/%s/' % (self.api_endpoint, endpoint), data=json.dumps(datas)).json()
        elif verb == 'get':
            return request.get('%s/%s/' % (self.api_endpoint, endpoint), params=params).json()

    def foursquare_venues(self):
        ''' Restricted by quotas...
        '''
        logging.debug('foursquare_venues')
        latlong = []
        venues = []

        if self.seeds:
            latlong = self.seeds
        else:
            # Fetch latest indexed venues if there's no seeds
            response = self.headbang('get', 'foursquare/venues', params={'size': 2, 'fields': 'location.lat,location.lng'})
            if response and 'error' not in response[0] and response[0]['_source']:
                location = response[0]['_source']['location']
                latlong.append('%s,%s' % (location['lat'], location['lng']))

        for ll in latlong:
            try:
                logging.debug(latlong)
                # Search for new venues around
                venues = venues + self.api_clients['foursquare'].search_venues(ll)['venues']
            except Exception as e:
                logging.error(e)

        # get uniq ids
        venues_ids = list(set([venue['id'] for venue in venues]))

        if venues_ids:
            for venue_id in venues_ids:
                # Fetch and index venues full informations
                venue = self.api_clients['foursquare'].get_venue(venue_id)
                response = self.headbang('post', 'foursquare/venues', datas=venue)
                time.sleep(0.5)
                logging.debug(response)

    def google_places(self):
        logging.debug('google_places')
        for venue in self.headbang('get', 'foursquare/venues'):
            name = venue['_source']['name']
            latlong = venue['_source']['location']['labeledLatLngs'][0]
            google_place = self.api_clients['google'].get_places(name, latlong)

            if google_place['results'] and 'place_id' in google_place['results'][0]:
                details = self.api_clients['google'].get_place_details(google_place['results'][0]['place_id'])
                if details and 'result' in details:
                    logging.info(details['result'])
                    response = self.headbang('post', 'google/places', datas=details['result'])
                    logging.debug(response)

    def facebook_places(self):
        logging.debug('facebook_places')
        for venue in self.headbang('get', 'foursquare/venues'):
            name = venue['_source']['name']
            latlong = '%s,%s' % (venue['_source']['location']['lat'], venue['_source']['location']['lng'])
            fb_places = self.api_clients['facebook'].get_places(name, latlong)

            if 'data' in fb_places and fb_places['data']:
                fbid = fb_places['data'][0]['id']
                details = self.api_clients['facebook'].get_place_details(fbid)
                response = self.headbang('post', 'facebook/places', datas=details)
                logging.debug(response)


if __name__ == '__main__':
    args = docopt(__doc__)
    getattr(Crawler(**args), args['--action'])()
