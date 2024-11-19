#!/bin/sh

function cleanup() {
    docker image prune --filter dangling=true -y
}

trap cleanup EXIT

docker compose up --build --force-recreate