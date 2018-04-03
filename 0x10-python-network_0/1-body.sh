#!/usr/bin/env bash
# Uses get request to return body of URL with 200 response
curl -siLX GET "$1" | tail -n1
