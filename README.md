# HEADBANG

## Generate playlists from incoming concerts
find concert places -> get associated fb events -> artists entity detection -> spotify matching -> tracks recommendations -> playlist generation

## Recommend concerts events based on your tastes
get similar venues and artists -> search for events

### Stack

- Docker
- Python Falcon API
- Elasticsearch
- Name entity recognition

#### Docker
Start the stack:

```bash
docker-compose up
```

This will setup an [Elasticsearch](http://localhost:9200) node,

Cerebro Elasticsearch admin
http://localhost:9000/#/overview?host=http:%2F%2Felasticsearch:9200

Kibana Sense console
http://localhost:5601/app/kibana#/dev_tools/console
