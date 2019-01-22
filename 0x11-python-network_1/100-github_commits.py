#!/usr/bin/python3
"""Python script that takes your Github repo and user)
 and uses the Github API to display commit name and sha number"""
import requests
import sys


def main():
    u = sys.argv[2]
    r = sys.argv[1]
    try:
        f_url = "https://api.github.com/repos/" + u + "/" + r + "/commits"
        req = requests.get(f_url)
        js = req.json()
        c = 0
        for d in js:
            print("{}: {}".format(d.get('sha'),
                  d.get('commit').get('author').get('name')))
            c += 1
            if c == 10:
                break
    except TypeError and KeyError:
        print("None")

if __name__ == "__main__":
    main()
