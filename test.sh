#!/bin/bash

type=$1
echo "$0: run $type test script"

./exec.sh src/$type/test_work.py -v

echo "$0: finish test script"