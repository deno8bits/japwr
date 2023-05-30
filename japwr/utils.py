import requests
from requests import Response


class ConnectionHandler:
    """
    Used for interacting with the Reddit API while also specifying consistant parameters
    which allows us to not have to specify certain parameters every time we use 'request'
    """
    def __init__(self, headers: dict, params: dict = {}) -> None:
        self.headers = {
            'Accpets': 'application/json'
        } | headers

        self.params = {} | params  # Used to specify global params eg. clientID and clientSecret for later

    def get(self, url: str, **kwargs) -> dict:

        params = self.params | kwargs

        rawReq = requests.get(url, params, headers=self.headers)

        self.checkError(rawReq)

        req = rawReq.json()

        return req

    def post(self, url: str, *kwargs) -> dict:
        raise Exception('Not Implemented Yet')

    def checkError(self, res: Response) -> None:
        print(vars(res.headers))

