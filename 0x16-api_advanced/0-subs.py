#!/usr/bin/python3
"""
find number of subscribers
"""
import requests as r


def number_of_subscribers(subreddit):
    """
    queries the Reddit API and returns the number of subscribers
    """
    headers = {"User-Agent": "Frocuts"}
    endpoint = "http://reddit.com/r/{}/about.json"
    subs = r.get(endpoint.format(subreddit), headers=headers)

    if subs.status_code != 200:
        return 0
    subs = subs.json()
    if subs["kind"] == "t5":
        return subs["data"]["subscribers"]
    else:
        return 0
