#!/bin/bash
#sends a Json POST request to the passed URL, and displays the body of the response
curl -s -X POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
