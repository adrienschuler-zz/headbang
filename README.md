# 🤘 HEADBANG 🤘

Where the f!ck can I HEADBANG tonight?!

## Concept

Generate personalized playlists from incoming concerts in your town and recommend events based on your tastes.

### Stack
- [Docker](https://www.docker.com/)
- [Python Flask API](http://flask.pocoo.org/)
- [Elasticsearch](https://www.elastic.co/)
- [Name entity recognition](https://github.com/Franck-Dernoncourt/NeuroNER)

### Configuration
Rename the [apis.yml.template](app/config/apis.yml.template) file in apis.yml and add your APIs keys (required by the crawler):
```yml
foursquare:
  client_id:
  client_secret:
facebook:
  app_id:
  app_secret:
  access_token:
google:
  api_key:
```

Also rename the [storage.yml.template](app/config/storage.yml.template) file in storage.yml.

### Install
Start the stack with docker compose:

```bash
docker-compose up
```

This will setup:
- [An Elasticsearch single node cluster](http://localhost:9200)
- [The Cerebro Elasticsearch admin](http://localhost:9000/#/overview?host=http:%2F%2Felasticsearch:9200)
- [The Kibana Sense console](http://localhost:5601/app/kibana#/dev_tools/console)
- [The Flask API](http://localhost:5000)

Or install the API locally (Python 3.6.4):
```bash
virtualenv -p python3 venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Setup Elasticsearch mappings:
```bash
./bin/setup_elasticsearch_mappings.sh
```

Start the Headbang API using [Gunicorn HTTP server](http://gunicorn.org/):
```bash
gunicorn --bind 0.0.0.0:5000 server:app --reload --log-level debug
```

### Crawler

Bootstrap Elasticsearch indices by scrapping Foursquare and Facebook APIs:

```bash
python crawler.py --foursquare_venues
python crawler.py --facebook_events
```

### API

#### Places

| HTTP Verb | API Endpoint                                | Description
| --------- | ------------------------------------------- | ------------
| `GET`     | /places?**size**=10&**fields**=lat,lng,fbid | Get [Foursquare Places](https://developer.foursquare.com/places-api) ranked by popularity
| `POST`    | /places                                     |

#### Events

| HTTP Verb | API Endpoint                | Description
| --------- | --------------------------- | ------------
| `GET`     | /events?**size**=10         | Get [Facebook Events](https://developers.facebook.com/docs/graph-api/reference/event)
| `POST`    | /events                     |
