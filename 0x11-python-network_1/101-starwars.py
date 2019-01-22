#!/usr/bin/python3
"""Python script that takes in a string and sends a search request to the
 Star Wars API """
import requests
import sys


def main():
    t_results = []
    full_url = 'https://swapi.co/api/people/?search=' + sys.argv[1]
    r = requests.get(full_url)
    js = r.json()
    t_results = t_results + js['results']
    while js['next'] is not None:
        print("Number of results: {}".format(js['count']))
        r = requests.get(js['next'])
        js = r.json()
        t_results = t_results + js['results']
    for x in t_results:
        print(x['name'])

if __name__ == "__main__":
    main()
