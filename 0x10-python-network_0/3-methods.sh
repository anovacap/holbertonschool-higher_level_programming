#!/usr/bin/env bash
#takes in a URL and displays all HTTP methods the server will accept.
curl -sI $1 | grep "Allow" | cut -f2,3,4 -d ' ' 
