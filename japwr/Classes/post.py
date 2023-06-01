class Post:
    """
        Post Object
    """

    # TODO: Check if there is a better way of mapping these vars
    # This will scale poorly
    def __init__(self, id: str = '', itemDict: dict = None) -> None:
        if itemDict:
            self.raw = itemDict  # Allow viewing the raw json
            item = itemDict['data']  # Wierd Mapping because the json is wierd
            self.isVideo: bool = item['is_video']
            self.isSelf: bool = item['is_self']
            self.title: str = item['title']
            self.score: int = item['score']
            self.url: str = item['url']
            self.id: str = item['id']
        else:
            # TODO get post info if itemDict is None
            raise Exception('Not Implemented')
        # self.author = None  # TODO: Implement a way of getting the author info in some way

    def __str__(self) -> str:
        return self.id

    def __repr__(self):
        return f'Post(id={self.id})'
