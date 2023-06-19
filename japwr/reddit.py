from japwr.utils import ConnectionHandler
from japwr.classes import Subreddit, MultiReddit
from japwr.auth import Auth


class Reddit:
    """Main class for initializing the stuff needed for everything else
    """
    def __init__(self, userAgent: str, clientID: str = '', clientSecret: str = '') -> None:
        """Initializes the Reddit class

        Args:
            userAgent (str): User-Agent used by Reddit to identify the client. Should be in this format `{App Name}:{Version} (by /u/{Username})`
            clientID (str, optional): ID used for oauth.
            clientSecret (str, optional): Secret used for oauth.
        """
        headers = {'User-Agent': userAgent}
        params = {}
        if clientID and clientSecret:
            auth = Auth(clientID, clientSecret)
            params = params | auth.getParams
        self.userAgent: str = userAgent

        self.connHandler = ConnectionHandler(headers, params)

    def subreddit(self, name: str) -> Subreddit:
        """Initializes a subreddit object
        
        Example::

            from japwr import Reddit
            r = Reddit("Some example useragent")
            sub = r.subreddit("examplesub")

        Args:
            name (str): Name of the subreddit (case-insensitive)

        Returns:
            Subreddit: Used to interact with the subreddit
        """
        sub = Subreddit(self.connHandler, name)

        return sub

    def multireddit(self, username: str, feedName: str) -> MultiReddit:
        """Initializes a MultiReddit(Custom feed) object

        Example::

            from japwr import Reddit
            r = Reddit("Some example useragent")
            sub = r.multireddit("someusername", "examplefeed")

        Args:
            username (str): Owner/Author of the MultiReddit
            feedName (str): Name of the MultiReddit

        Returns:
            MultiReddit: Used to interact with the MultiReddit
        """
        feed = MultiReddit(self.connHandler, username, feedName)

        return feed
