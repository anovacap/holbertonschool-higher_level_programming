#!/usr/bin/python3
"""Python script that takes in a string and sends a search request to the
 Star Wars API """
import requests
import sys


def main():
    full_url = 'https://swapi.co/api/people/?search=' + sys.argv[1]
    r = requests.get(full_url)
    js = r.json()
    print("Number of results: {}".format(js['count']))
    for x in js['results']:
        print(x['name'])

if __name__ == "__main__":
    main()
