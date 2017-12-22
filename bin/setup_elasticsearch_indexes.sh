#!/bin/sh
cd mappings

for mapping in `ls`; do
    index=`echo $mapping | sed -E 's/\.json//g'`
    curl -H'Content-Type: application/json' -XPUT "localhost:9200/$index" -d @"$mapping"
done
