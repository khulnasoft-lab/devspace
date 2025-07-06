#!/bin/bash

set -e

docker build \
       --file docker/benchmark.Dockerfile \
       -t devspace-benchmark \
       .
