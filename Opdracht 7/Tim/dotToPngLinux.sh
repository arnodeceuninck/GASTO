#!/usr/bin/env bash

for f in *.dot
do
  echo "Processing $f file..."
  dot -Tpng "$f" -o "$f.png"
done