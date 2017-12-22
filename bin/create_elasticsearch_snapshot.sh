curl -XPUT "http://localhost:9200/_snapshot/headbang/snapshot_2?wait_for_completion=true" -H 'Content-Type: application/json' -d'
{
  "indices": ".kibana,foursquare.venues,facebook.events",
  "ignore_unavailable": true,
  "include_global_state": false
}'

tar -cvzf snapshots/headbang.tar.gz /usr/local/var/lib/elasticsearch/snapshots/headbang

