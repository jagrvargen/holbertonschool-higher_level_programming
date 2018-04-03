#!/bin/bash
# Sends a POST request to a URL adding email and subject data.
curl -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
