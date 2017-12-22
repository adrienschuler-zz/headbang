# HEADBANG

## Generate playlists from incoming concerts
find concert places -> get associated fb events -> artists entity detection -> spotify matching -> tracks recommendations -> playlist generation

## Recommend events based on your tastes
get similar venues
get similar artists -> search for events

### foursquare venues
venues/search?intent=browse&ll=48.85361,2.37455&radius=15000&limit=50&categoryId=4bf58dd8d48988d1e5931735,5032792091d4c4b30a586d5c

### facebook access token
curl -XGET "https://graph.facebook.com/oauth/access_token?client_id={}&client_secret={}&grant_type=client_credentials"

### facebook events
180056048702133/events?fields=attending_count,can_guests_invite,can_viewer_post,category,cover,declined_count,description,end_time,event_times,guest_list_enabled,interested_count,maybe_count,name,place,ticket_uri,is_canceled,id,is_draft,is_page_owned,is_viewer_admin,owner,noreply_count,parent_group,ticketing_terms_uri,timezone,type,ticketing_privacy_uri,updated_time,start_time.order(chronological)&since=1513858364

### APIs

- venues
    - yelp
    - tripadvisor
    - foursquare
- events
    - facebook
    - songkick
    - bandsintown
    - digitick
    - residentadvisor
    - ticketswap
- artists
    - bandcamp
    - spotify
    - deezer
    - youtube
    - discogs
    - musicbrainz
    - twitter
    - google knowledge graph


### Stack

- Docker
- Flask API
- Elasticsearch
- Name entity recognition


#### Docker
Start the stack:

```bash
docker-compose up
```

Cerebro ES admin:
http://localhost:9000/#/overview?host=http:%2F%2Felasticsearch:9200


