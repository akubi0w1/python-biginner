#!/bin/bash

if [ "$1" = "" ]; then
    echo "need arg: file path"
    exit 1
fi

# exexute python
docker exec python3 python $1 ${@:2}