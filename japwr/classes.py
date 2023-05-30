from japwr.utils import ConnectionHandler
"""
TODO: Implement a better way of handling feeds (Subreddit, Multireddit etc.)
ref:
    https://www.reddit.com/dev/api#section_listings

Multireddits also use /new /hot etc for its stuff so a parent class might be a good idea for handling feeds
to avoid repeating alot of code
"""


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
    # TODO: Figure out how to actually interact with multireddits using the api
    # Either the API docs for this is unclear or I'm an idiot
    # refs:
    #   https://www.reddit.com/dev/api#section_multis
    #   https://www.reddit.com/dev/api#section_listings
    #
    # 2023/05/30 10:38:
    # multipath = /user/<username>/m/<name>
    # /top /hot /best etc. don't work at the end it just returns 404 saying the feed was not found
    # Will try with clientID and clientSecret might just be wierd
    #
    # 2023/05/30 10:42: ^ no
    # I don't know how in the absolute hell your supposed to get posts.
    #
    # 2023/05/30 11:12: There are no words to describe the absolute fury I'm feeling
    # According to the documentation the url for multis are https://api.reddit.com/api/multi/<multipath>
    # BUT no where in the documentation does it mention the place where you get the listing (posts) from the api
    #
    # So I went digging in PRAWs code which did not really give a solution but it put me on the correct path
    #
    # The url for gettings posts from the api for multireddits is https://api.reddit.com/<multipath>
    #
    # I don't know why they did it like this nor do I know why its not in the documention but here it is.
    #
    # This took way longer then it should have and I'm never getting back the ~30 mins I spent looking for
    # this damned url
    #
    """
    Creates a MultiReddit Instance
    """
    def __init__(self, connHandler: ConnectionHandler, username, feedName) -> None:
        self.username = username
        self.feedName = feedName
        self.connHandler = connHandler
        self.urlBase = f'https://api.reddit.com/user/{username}/m/{feedName}/'
        raise Exception('Not Implemented Yet')

    def new(self, limit: int = 25) -> dict:

        return
