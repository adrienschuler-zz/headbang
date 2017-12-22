import facebook


class Facebook:

    def __init__(self, config):
        self.graph = facebook.GraphAPI(access_token=config['access_token'])

    def get_events(self, object_id):
        fields = 'attending_count,can_guests_invite,can_viewer_post,category,cover,declined_count,description,end_time,event_times,guest_list_enabled,interested_count,maybe_count,name,place,ticket_uri,is_canceled,id,is_draft,is_page_owned,is_viewer_admin,owner,noreply_count,parent_group,ticketing_terms_uri,timezone,type,ticketing_privacy_uri,updated_time,start_time.order(chronological)'
        args = {
            'include_canceled': 'false',
            'time_filter': 'upcoming'
        }

        return self.graph.get_object('%s/events' % str(object_id), fields=fields, args=args)
