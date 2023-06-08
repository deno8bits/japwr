# TODO: Implement authentication stuff
class Auth:
    def __init__(self, clientID: str, clientSecret: str) -> None:
        self.clientID = clientID
        self.clinetSecret = clientSecret

    def getParams(self) -> dict[str]:
        return {
            'client_id': self.clientID,
            'client_secret': self.clinetSecret
        }
