#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and
 displays the value of the X - Request - Id """
import urllib.request
import sys


def main():
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.getheaders()
        for tup in html:
            if 'X-Request-Id' in tup:
                print(tup[1])

if __name__ == "__main__":
    main()
