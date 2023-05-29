from japwr.utils import ConnectionHandler
from japwr.classes import Subreddit, MultiReddit


class Reddit:
    def __init__(self, userAgent: str) -> None:
        self.userAgent: str = userAgent
        self.connHandler = ConnectionHandler({'user_agent': self.userAgent})

    def subreddit(self, name) -> Subreddit:
        sub = Subreddit(self.connHandler, name)

        return sub

    def multireddit(self, username, feedName) -> MultiReddit:
        feed = MultiReddit(self.connHandler, username, feedName)

        return feed
