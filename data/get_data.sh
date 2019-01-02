#!/usr/bin/env bash

wget -r -nH -nc -np --cut-dirs=100 -A "secom*" \
http://archive.ics.uci.edu/ml/machine-learning-databases/secom/ \

echo "Additional JSON needs to be added manually"
