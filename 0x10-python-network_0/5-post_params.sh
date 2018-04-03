#!/bin/bash
# Sends a POST request to a URL adding email and subject data.
curl -X POST "$1" -F "email=hr@holbertonschool.com" -F "subject=I+will+always+be+here+for+PLD" 
