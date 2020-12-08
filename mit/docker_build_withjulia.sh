#!/usr/bin/env bash

set -x

cd ..

# Add --no-cache to make it start from scratch
# docker build --no-cache --progress plain -f mit/combined_withjulia.dockerfile -t combined_withjulia:latest .

docker build -f mit/combined_withjulia.dockerfile -t combined_withjulia:latest .
