#!/bin/bash
#displays the size of the body of the response of a given url
curl -s "$1" | wc -c
