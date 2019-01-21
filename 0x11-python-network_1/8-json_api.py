#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
 http: // 0.0 .0 .0: 5000 / search_user with the letter as a parameter """
import requests
import sys


def main():
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    data = {'q': q}
    r = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        js = r.json()
        id = js.get('id')
        name = js.get('name')
        if id is None or name is None:
            print("No result")
        else:
            print("[{}] {}".format(id, name))
    except:
        print("Not a valid JSON")

if __name__ == "__main__":
    main()
