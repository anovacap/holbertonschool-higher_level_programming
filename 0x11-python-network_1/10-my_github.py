#!/usr/bin/python3
"""Python script that takes your Github credentials (username and password)
 and uses the Github API to display your id """
import requests
import sys


def main():
    try:
        r = requests.get("https://api.github."
                         "com/user", auth=(sys.argv[1], sys.argv[2]))
        js = r.json()
        print(js['id'])
    except TypeError and KeyError:
        print("None")

if __name__ == "__main__":
    main()
