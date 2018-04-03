#!/bin/bash
# Sends a POST request to a URL adding email and subject data.
curl -X POST "$1" -d "email=hr@holbertonschool.com&subject=I+will+always+be+here+for+PLD" 
