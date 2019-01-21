#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays
 the body of the response - manage urllib.error.HTTPError exceptions and
  print: Error code: followed by the HTTP status code """
import urllib.request
import sys


def main():
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read().decode('utf-8')
            print(html)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))

if __name__ == "__main__":
    main()
