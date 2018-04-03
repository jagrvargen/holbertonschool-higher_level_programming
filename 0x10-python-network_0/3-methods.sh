#!/bin/bash
# Displays all methods accepted by a URL passed as first argument.
curl -sILX OPTIONS "$1" | grep Allow: | cut -d " " -f2-
