#!/bin/sh
nginx -c "$(pwd)/nginx/ssi-termux.conf" -g "daemon off;"
