#!/usr/bin/python3
"""Python script that takes in 3 strings and sends a search request
 to the Twitter API """
import base64
import requests
import sys


def main():
    key_secret = "{}:{}".format(sys.argv[1], sys.argv[2]).encode('ascii')
    encd_key = base64.b64encode(key_secret)
    encd_key = encd_key.decode('ascii')
    base_url = "https://api.twitter.com/"
    auth_url = "{}oauth2/token".format(base_url)
    auth_headers = {
        "Authorization": "Basic {}".format(encd_key),
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
    }
    auth_data = {
        "grant_type": "client_credentials"
    }
    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)
    access_token = auth_resp.json()['access_token']
    search_headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }
    search_params = {
        'q': sys.argv[3],
        'count': 5
    }
    search_url = '{}1.1/search/tweets.json'.format(base_url)
    search_resp = requests.get(search_url, headers=search_headers,
                               params=search_params)
    tweet_data = search_resp.json()
    for x in tweet_data['statuses']:
        print("[{}] {} by {}".format(x['id_str'],
              x['text'], x['user']['name']))

if __name__ == "__main__":
    main()
