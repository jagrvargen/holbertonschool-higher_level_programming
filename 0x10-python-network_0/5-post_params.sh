#!/bin/bash
# Sends a POST request to a URL adding email and subject data.
curl -d "email=hr@holbertonschool.com&subject=I+will+always+be+here+for+PLD"\
-X POST "$!"
