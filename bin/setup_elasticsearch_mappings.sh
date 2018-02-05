#!/bin/sh
cd datas/mappings

for mapping in `ls`; do
    index=`echo $mapping | sed -E 's/\.json//g'`
    echo $index
    echo `curl -s -H'Content-Type: application/json' -XPUT "localhost:9200/$index" -d @"$mapping"`
done
