#!/bin/sh
cd mappings

for mapping in `ls`; do
    index=`echo $mapping | sed -E 's/\.json//g'`
    curl -H'Content-Type: application/json' -XPUT "localhost:9200/$index" -d @"$mapping"
done

curl -XPUT "http://localhost:9200/_all/_settings" -H 'Content-Type: application/json' -d'
{
    "index" : {
        "number_of_replicas" : 0
    }
}'
