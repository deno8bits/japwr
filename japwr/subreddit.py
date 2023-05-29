import requests
from japwr.reddit import Reddit
from japwr.post import Post
import japwr.error


class Subreddit:
    def __init__(self, reddit: Reddit, name: str):
        self.name = name
        self.headers = {
            'Accept': 'application/json',
            'User-Agent': reddit.userAgent
        }

    def new(self, limit: int = 25) -> list[Post]:
        """
        Gets new posts

        Args:
            limit: int

        Returns:
            posts: Post
        """

        params = {
            'limit': limit
        }

        req = requests.get(f'https://api.reddit.com/r/{self.name}/new', params, headers=self.headers,).json()

        # TODO: Error checking before this point otherwise this will fail badly
        try:
            posts = [Post(item) for item in req['data']['children']]
        except KeyError:
            if req['error'] == 403:
                raise japwr.error.Unauthorized()
            else:
                raise Exception(req['message'])

        return posts
