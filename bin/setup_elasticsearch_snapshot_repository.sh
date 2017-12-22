# TODO: add path.repo in elasticsearch.yml conf
curl -XPUT "http://localhost:9200/_snapshot/headbang" -H 'Content-Type: application/json' -d'
{
  "type": "fs",
  "settings": {
    "location": "/usr/local/var/lib/elasticsearch/snapshots/headbang",
    "compress": true
  }
}'
