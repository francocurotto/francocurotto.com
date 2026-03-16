#!/bin/sh
nginx -c "$(pwd)/nginx/ssi.conf" -g "daemon off;"
