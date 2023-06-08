from japwr.utils import ConnectionHandler
from .Classes.listingBase import ListingBase


class Subreddit:
    """
    Creates a Subreddit Instance
    """
    def __init__(self, connHandler: ConnectionHandler, name: str):
        self.name = name
        self.connHandler = connHandler
        self.urlBase = f'https://api.reddit.com/r/{self.name}'


class MultiReddit(ListingBase):
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
        self.urlBase = f'https://api.reddit.com/user/{username}/m/{feedName}'
