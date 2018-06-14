import facebook

from app import logging
from app.utils import remove_duplicates


class Facebook:

    def __init__(self, config: dict):
        self.graph = facebook.GraphAPI(access_token=config['access_token'], version='3.0')

    def get_events(self, object_id: str) -> dict:
        fields = 'attending_count,can_guests_invite,can_viewer_post,category,cover,declined_count,description,end_time,event_times,guest_list_enabled,interested_count,maybe_count,name,place,ticket_uri,is_canceled,id,is_draft,is_page_owned,is_viewer_admin,owner,noreply_count,parent_group,ticketing_terms_uri,timezone,type,ticketing_privacy_uri,updated_time,start_time.order(chronological)'

        args = {
            'include_canceled': 'false',
            'time_filter': 'upcoming'
        }

        return self.graph.get_object(
            '%s/events' % object_id,
            fields=fields,
            args=args
        )

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
