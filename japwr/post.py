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
