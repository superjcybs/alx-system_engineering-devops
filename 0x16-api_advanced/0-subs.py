#!/usr/bin/python3
"""
TASK: To query total subscribers on a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Return: total number of subscribers on a given subreddit or return 0
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    sub_r_subscribers = requests.get(url,
                                     headers=headers,
                                     allow_redirects=False
                                     )
    if sub_r_subscribers.status_code >= 300:
        return 0
    return sub_r_subscribers.json().get("data").get("subscribers", 0)


print(number_of_subscribers("programming"))
