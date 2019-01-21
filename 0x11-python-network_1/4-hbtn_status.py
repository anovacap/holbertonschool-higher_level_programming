#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status"""
import requests


def main():
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}\n\t- content: "
          "{}".format(type(r.text), r.content.decode('utf-8')))

if __name__ == "__main__":
    main()
