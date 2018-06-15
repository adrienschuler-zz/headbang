import facebook

from app import logging
from app.utils import remove_duplicates


class Facebook:

    def __init__(self, config: dict):
        self.graph = facebook.GraphAPI(access_token=config['access_token'], version='3.0')

    def get_places(self, query: str, latlong: str) -> dict:
        return self.graph.search(
            type='place',
            q=query,
            center=latlong,
            distance=1000
        )

    def get_place_details(self, fbid):
        fields = 'about,app_links,category_list,checkins,cover,description,engagement,hours,is_always_open,is_permanently_closed,is_verified,link,location,name,overall_star_rating,parking,payment_options,phone,photos,picture,price_range,rating_count,restaurant_services,restaurant_specialties,single_line_address,website,workflows'
        return self.graph.get_object(
            id=str(fbid),
            fields=fields
        )
