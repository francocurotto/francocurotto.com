#!/bin/sh
DIR="$(cd "$(dirname "$0")" && pwd)"
nginx -p "$DIR" -c "$DIR/nginx/ssi-local.conf" -g "daemon off;"
