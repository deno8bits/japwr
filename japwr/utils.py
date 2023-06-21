# FIXME: Add better docs here to make future development faster
import requests
from requests import Response
from japwr import error


class ConnectionHandler:
    """
    Used for interacting with the Reddit API while also specifying consistant parameters
    which allows us to not have to specify certain parameters every time we use 'request'

    Examples::

        conn = ConnectionHandler(header={headers here}, params={paramshere})
        conn.get(url, {additional args})

    """
    def __init__(self, headers: dict, params: dict = {}) -> None:
        """Initializes a ConnectionHandler

        Args:
            headers (dict): Global Headers to add, Required for the UserAgent
            params (dict, optional): Global Params to add (eg. clientID and clientSecret). Defaults to {}.
        """
        self.headers = {
            'Accpets': 'application/json'
        } | headers  # Adds to the global headers, required to add UserAgent

        self.params = {} | params  # Used to specify global params eg. clientID and clientSecret for later

    def get(self, url: str, **kwargs) -> dict:
        """Sends a get request to the specified url and uses the global headers and params

        Use kwargs to add extra params

        Args:
            url (str): URL to send request to
            **kwargs (): Extra params to send with the global ones

        Returns:
            dict: Returns the parsed response JSON
        """

        params = self.params | kwargs

        rawReq = requests.get(url, params, headers=self.headers)

        self.checkError(rawReq)

        req = rawReq.json()

        return req

    def post(self, url: str, *kwargs) -> dict:
        """Not Implemented Yet

        Will be used to change stuff

        Args:
            url (str): _description_

        Raises:
            Exception: _description_

        Returns:
            dict: _description_
        """
        raise Exception('Not Implemented Yet')

    def checkError(self, res: Response) -> None:
        """_summary_

        Args:
            res (Response): Response to check if it errored out.

        Raises:
            error.Unauthorized: Got a 403
            error.RateLimited: Was Ratelimited
            Exception: Got a error that was not implemented by the wrapper yet.
        """
        if res.status_code != 200:
            match res.status_code:
                case 403:
                    # TODO: Add a check to see if the instance is authorized to make the error messages more useful
                    raise error.Unauthorized()

                case 429:
                    raise error.RateLimited()

                case _:
                    print(res.json())
                    raise Exception(res.json()['message'])

        return
