#!/bin/bash
# Displays only status code of an HTTP get request.
curl -sw %{http_code} "$1" -o /dev/null
