#!/usr/bin/env bash

set -x

cd ..

docker build --no-cache --progress plain -f mit/combined_withjulia.dockerfile -t combined_withjulia:latest .
