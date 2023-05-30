from japwr.utils import ConnectionHandler
import japwr.error


class Post:
    """
        Post Object
    """

    # TODO: Check if there is a better way of mapping these vars
    # This will scale poorly
    def __init__(self, item: dict) -> None:
        self.raw = item  # Allow viewing the raw json
        item = item['data']  # Wierd Mapping because the json is wierd
        self.isVideo: bool = item['is_video']
        self.isSelf: bool = item['is_self']
        self.title: str = item['title']
        self.score: int = item['score']
        self.url: str = item['url']
        # self.author = None  # TODO: Implement a way of getting the author info in some way


class Subreddit:
    """
    Creates a Subreddit Instance
    """
    def __init__(self, connHandler: ConnectionHandler, name: str):
        self.name = name
        self.connHandler = connHandler

    def new(self, limit: int = 25) -> list[Post]:
        """
        Gets new posts

        Args:
            limit: int

        Returns:
            posts: Post
        """
        # Error handling for this is implemented at the ConnectionHandler
        req = self.connHandler.get(f'https://api.reddit.com/r/{self.name}/new', limit=limit)

        return [Post(item) for item in req['data']['children']]


class MultiReddit:
    """
    Creates a MultiReddit Instance
    """
    def __init__(self, connHandler: ConnectionHandler, username, feedName) -> None:
        self.username = username
        self.feedName = feedName
        self.connHandler = connHandler

    def new(self, limit: int = 25) -> dict:

        return
