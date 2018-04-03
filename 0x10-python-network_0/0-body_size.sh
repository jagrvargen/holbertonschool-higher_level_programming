#!/usr/bin/env bash
# Takes in a URL, sends a request to it, and displays the size of the body.
curl -sI 0.0.0.0:5000 | grep Content-Length: | cut -d " " -f2
