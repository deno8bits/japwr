import requests
import json
from japwr.reddit import Reddit


class Subreddit:
    def __init__(self, reddit: Reddit, name: str):
        self.name = name
        self.headers = {
            'Accept': 'application/json',
            'User-Agent': reddit.userAgent
        }

    def new(self, limit: int = 25) -> list[dict]:
        """
        Gets new posts

        Args:
            limit: int

        Returns:
            posts: dict
        """
        
        params = {
            'limit': limit
        }

        req = requests.get(f'https://api.reddit.com/r/{self.name}/new', params, headers=self.headers,).json()

        return req['data']['children']
