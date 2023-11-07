#!/usr/bin/python3
"""0-subs"""
import requests


def number_of_subscribers(subreddit):
    """return the number of subscribers"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    header = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        json_data = response.json()
        num = json_data.get('data').get('subscribers')
        if num:
            return num
        else:
            return 0
    else:
        return 0
