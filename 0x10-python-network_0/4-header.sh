#!/bin/bash
# Sends a GET request to a URL with a header variable to retrieve body.
curl -H "X-HolbertonSchool-User-Id: 98" -X GET "$1"
