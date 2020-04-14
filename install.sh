#!/bin/bash

# install python package
docker exec python3 pip install ${@:1}