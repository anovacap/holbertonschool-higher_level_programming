#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request to the passed URL
 with the email as a parameter, and displays the body of the response
  (decoded in utf - 8) """
import urllib.request
import urllib.parse
import sys


def main():
    values = {'email': sys.argv[2]}
    email = urllib.parse.urlencode(values)
    email = email.encode('ascii')
    req = urllib.request.Request(sys.argv[1], email)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    print(the_page.decode('utf-8'))

if __name__ == "__main__":
    main()
