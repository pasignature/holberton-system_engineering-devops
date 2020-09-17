#!/usr/bin/python3
"""
recursive
"""
import requests as r


def recurse(subreddit, hot_list=[], key=""):
    """
    recursive function that queries the Reddit API and 
	returns a list containing the titles of all hot articles
    """
    if (subreddit is not None):
        h = {"User-Agent": "Frocuts"}
        endpoint = "http://reddit.com/r/{}/hot.json"
        p = {'after': key}
        subs = r.get(endpoint.format(subreddit), headers=h, params=p)
        if subs.status_code != 200:
            return None
        subs = subs.json()
        # hot_list.extend(subs["data"]["children"])
        hot_list.extend([x.get('data').get('title')
                        for x in subs["data"]["children"]])
        if subs['data']['after'] is not None:
            recurse(subreddit, hot_list, subs['data']['after'])
        if (len(hot_list) > 0):
            return hot_list
        return None
    else:
        return None
