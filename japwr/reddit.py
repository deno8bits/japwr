from japwr.utils import ConnectionHandler
from japwr.classes import Subreddit, MultiReddit
from japwr.auth import Auth


class Reddit:
    def __init__(self, userAgent: str, clientID: str = '', clientSecret: str = '') -> None:
        headers = {'User-Agent': userAgent}
        params = {}
        if clientID and clientSecret:
            auth = Auth(clientID, clientSecret)
            params = params | auth.getParams
        self.userAgent: str = userAgent

        self.connHandler = ConnectionHandler(headers, params)

    def subreddit(self, name) -> Subreddit:
        sub = Subreddit(self.connHandler, name)

        return sub

    def multireddit(self, username, feedName) -> MultiReddit:
        feed = MultiReddit(self.connHandler, username, feedName)

        return feed
