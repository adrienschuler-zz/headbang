curl -XPUT "http://localhost:9200/_snapshot/headbang/first?wait_for_completion=true" -H 'Content-Type: application/json' -d'
{
  "indices": "foursquare.venues,facebook.events",
  "ignore_unavailable": true,
  "include_global_state": false
}'

# tar -cvzf snapshots/headbang.tar.gz && cp usr/share/elasticsearch/snapshots /usr/share/elasticsearch/snapshots
