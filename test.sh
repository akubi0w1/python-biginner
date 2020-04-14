#!/bin/bash

type=$1
if [ "$type" = "" ]; then
    echo "need arg: list, dict, loop or map"
    exit 1
fi

echo "$0: run $type test script"

./exec.sh src/$type/test_work.py -v

echo "$0: finish test script"