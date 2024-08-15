#!/usr/bin/python3
import requests

"""TASK: To query total subscribers on a given subreddit"""

def number_of_subscribers(subreddit):
    """Return: total number of subscribers on a given subreddit or return 0"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "My-User-Agent"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0

    try:
        results = response.json().get("data")
        return results.get("subscribers", 0)
    except( ValueError, AttributeError):
        return 0    

print(number_of_subscribers("programming"))